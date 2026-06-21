# Cursor IDE Tool Integration Assignment

## Tools Installed
* **Cursor IDE:** Installed and configured the main editor environment.
* **Claude Code CLI:** Installed globally via npm (`@anthropic-ai/claude-code`) and verified fully active and logged into my Anthropic organization workspace via the terminal.
* **Codex Extension:** Installed the official OpenAI coding agent extension bundle (`openai.chatgpt`).

## Steps Completed
1. Initialized local project tracking workspace inside Cursor IDE.
2. Verified global compilation, tool activation, and runtime session stability for Claude Code inside the integrated terminal.
3. Repositioned Cursor's underlying workbench activity layout to a vertical format to expose hidden tool windows.
4. Activated the Codex extension window panel and successfully logged into the active interface context.
5. Setup a public GitHub repository link for upstream tracking.

## Issues Encountered & Solutions

### 1. Inaccessible Codex UI Elements
* **Issue:** Cursor's custom default display compresses standard extension sidebars, keeping the Codex panels and sign-in frames completely hidden from view.
* **Solution:** Opened the underlying application preferences tree, isolated the `Workbench › Activity Bar: Location` configuration, and forced it to `vertical`. Restarted the editor environment to cleanly project the missing OpenAI interface tile and trigger the workspace login panel.

---

# Phase 2: Research Project — Newsletter & Email Marketing for B2B SaaS

## Topic Selection & Strategic Rationale
I selected **Newsletter / Email Marketing for B2B SaaS** because owned audiences represent the highest leverage channel for modern SaaS companies. With rising customer acquisition costs (CAC) on paid ad platforms, building a high-signal newsletter engine enables predictable, zero-marginal-cost distribution and direct-to-buyer relationship building.

## Technical Data Collection Workflow
To gather raw data programmatically without relies on locked native interfaces, I executed an automated data pipeline within this repository:
1. **Source Mapping:** Curated 11 elite, practitioner-level experts inside `/research/sources.md`.
2. **Automated Transcript Extraction:** Developed and executed a custom Python script using `youtube-transcript-api` to pull raw video data for identified experts, automatically cleaning and parsing the outputs into human-readable files named by expert inside `/research/youtube-transcripts/`.
3. **Manual Content Curation:** Supplemented the data engine by pulling high-signal tactical frameworks from top creators' primary text feeds into `/research/linkedin-posts/`.

---

## 💡 Key Research Takeaways & Learnings

Through deep indexing of the transcripts and expert frameworks, I have distilled four foundational pillars required to build a world-class B2B SaaS newsletter playbook:

### 1. The "Product" Mindset (Emily Kramer, Tyler Denk)
* **The Learning:** A B2B newsletter will fail if treated as a PR dumping ground for company updates or funding announcements. 
* **The Playbook Action:** Treat the newsletter as a standalone media product providing utility independent of the software. It must maintain a predictable weekly format (e.g., *1 Deep Dive + 2 Tactical Tools*) focused on solving a specific, systemic user problem.

### 2. Behavioral Triggers Over Calendar Blasts (Jane Portman, Chris Frantz, Val Geisler)
* **The Learning:** Time-based drip sequences (Day 1, Day 3, Day 7) are fundamentally broken for B2B SaaS. Users convert based on product milestones, not the calendar.
* **The Playbook Action:** Align email automation with product usage data. If a user drops off before hitting their "Aha! Moment" (e.g., connecting a data source), trigger an automated behavioral nudge offering a 60-second video solution instead of a generic coupon.

### 3. Account-Level Segmentation (Jane Portman)
* **The Learning:** B2B SaaS architectures must differentiate between the *Account* (the company) and the *User* (the individual employee). Blasting a manager with a basic feature onboarding tip when their developer has already fully implemented it breaks brand trust.
* **The Playbook Action:** Pass company-wide app metrics to the ESP. Segment messaging strictly by user role: executive buyers receive high-level ROI case studies, while end-user developers receive workflow shortcuts and technical documentation.

### 4. Audience Curation & Lifecycle Guardrails (Brennan Dunn, Matt McGarry)
* **The Learning:** High volume means nothing if the signal-to-noise ratio is weak. Newsletters must protect active onboarding and retention experiences.
* **The Playbook Action:** Implement hard suppression rules. If a prospective customer is currently active inside a 14-day trial onboarding flow, automatically suppress them from receiving the global marketing newsletter until they exit the funnel.

---

## Repository Architecture
```text
├── research/
│   ├── linkedin-posts/         # Curated tactical frameworks from core experts
│   ├── youtube-transcripts/    # Programmatically extracted markdown transcripts
│   └── sources.md              # Master directory of 11 vetted practitioners & annotations
├── fetch_youtube_transcripts.py # Custom Python automation engine
└── README.md                   # Setup documentation & research executive summary