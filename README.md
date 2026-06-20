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