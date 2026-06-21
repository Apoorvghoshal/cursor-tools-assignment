"""Download transcripts for YouTube URLs listed in research/sources.md."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from youtube_transcript_api import YouTubeTranscriptApi


ROOT = Path(__file__).resolve().parent
SOURCES_FILE = ROOT / "research" / "sources.md"
OUTPUT_DIR = ROOT / "research" / "youtube-transcripts"
URL_PATTERN = re.compile(r"https?://(?:www\.)?(?:youtube\.com|youtu\.be)/[^\s)>]+")
VIDEO_ID_PATTERN = re.compile(r"^[A-Za-z0-9_-]{11}$")


def youtube_urls(markdown: str) -> list[str]:
    """Return unique YouTube URLs from Markdown, preserving their order."""
    return list(dict.fromkeys(URL_PATTERN.findall(markdown)))


def video_id_from_url(url: str) -> str | None:
    """Extract an ID from watch, short, embed, live, or youtu.be URLs."""
    parsed = urlparse(url)
    host = parsed.netloc.lower().removeprefix("www.")

    if host == "youtu.be":
        candidate = parsed.path.strip("/").split("/")[0]
    elif parsed.path == "/watch":
        candidate = parse_qs(parsed.query).get("v", [""])[0]
    elif parsed.path.startswith(("/shorts/", "/embed/", "/live/")):
        candidate = parsed.path.strip("/").split("/")[1]
    else:
        return None

    return candidate if VIDEO_ID_PATTERN.fullmatch(candidate) else None


def transcript_text(video_id: str) -> str:
    """Fetch a transcript and combine its snippets into readable paragraphs."""
    transcript = YouTubeTranscriptApi().fetch(video_id, languages=["en"])
    return "\n\n".join(
        snippet.text.strip() for snippet in transcript if snippet.text.strip()
    )


def main() -> None:
    if not SOURCES_FILE.exists():
        raise SystemExit(f"Sources file not found: {SOURCES_FILE}")

    urls = youtube_urls(SOURCES_FILE.read_text(encoding="utf-8"))
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if not urls:
        raise SystemExit(f"No YouTube URLs found in {SOURCES_FILE}")

    saved = 0
    for url in urls:
        video_id = video_id_from_url(url)
        if video_id is None:
            print(f"Skipping non-video URL: {url}")
            continue

        try:
            text = transcript_text(video_id)
            output_file = OUTPUT_DIR / f"{video_id}.md"
            output_file.write_text(
                f"# YouTube Transcript: {video_id}\n\n"
                f"Source: {url}\n\n"
                f"## Transcript\n\n{text}\n",
                encoding="utf-8",
            )
            saved += 1
            print(f"Saved {output_file}")
        except Exception as error:
            # A disabled or unavailable transcript should not stop other videos.
            print(f"Could not fetch {url}: {error}")

    print(f"Done: saved {saved} transcript(s) to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
