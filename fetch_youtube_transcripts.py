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


def expert_youtube_urls(markdown: str) -> list[tuple[str, str]]:
    """Extract expert names and their first corresponding YouTube URL from Markdown."""
    mapping = []
    
    # Split the markdown document by the expert headers (e.g., "## 1. Brendan Hufford")
    blocks = markdown.split("## ")
    
    for block in blocks[1:]:  # Skip the introductory table block
        lines = block.strip().split("\n")
        if not lines:
            continue
            
        # Extract the name from the header line, removing the "1. " prefix
        raw_name = re.sub(r"^\d+\.\s*", "", lines[0]).strip()
        # Create a clean, slugified filename (e.g., "Brendan Hufford" -> "brendan-hufford")
        safe_name = re.sub(r"[^a-z0-9]+", "-", raw_name.lower()).strip("-")
        
        # Find all YouTube URLs under this expert's section
        urls = list(dict.fromkeys(URL_PATTERN.findall(block)))
        if urls:
            mapping.append((safe_name, urls[0]))
            
    return mapping


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

    expert_urls = expert_youtube_urls(SOURCES_FILE.read_text(encoding="utf-8"))
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if not expert_urls:
        raise SystemExit(f"No YouTube URLs found in {SOURCES_FILE}")

    saved = 0
    for expert_name, url in expert_urls:
        video_id = video_id_from_url(url)
        if video_id is None:
            print(f"Skipping non-video URL: {url}")
            continue

        try:
            text = transcript_text(video_id)
            # Use the expert's name for the output file
            output_file = OUTPUT_DIR / f"{expert_name}.md"
            
            # Format the title back to normal text for the internal heading
            display_name = expert_name.replace('-', ' ').title()
            
            output_file.write_text(
                f"# YouTube Transcript: {display_name}\n\n"
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