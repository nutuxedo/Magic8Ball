<!-- .github/copilot-instructions.md: Project-specific guidance for AI coding agents -->
# Magic8Ball — Copilot instructions

Keep suggestions tightly scoped to small, low-risk edits unless asked for larger refactors. This repository is a tiny Tkinter-based Python toy app. The guidance below prioritizes making safe, runnable changes and documenting UI behavior.

- Project entry points and key files
  - `src/8ball_src.py` — main Tkinter UI and program behavior (EightBall class, `mainwindow()` function). This is the primary file to edit for UI, button actions, and answers list.
  - `src/dump.py` — small playground script showing how `PhotoImage` is loaded from `imgs/Magic_eight_ball.png`.
  - `README.md` — one-line description only; no build instructions.

- Big-picture architecture
  - Single-process desktop GUI using Tkinter. There is no backend server, packaging, or tests. The UI is created and started in `mainwindow()`; `EightBall` is a simple stateful helper that returns random answers.
  - Data flow: UI button triggers `EightBall().shake()` which sleeps 2s then returns a random answer. UI currently prints answers to stdout rather than rendering them in the window.

- Coding conventions & observable patterns
  - Minimal, imperative style: functions create Tkinter widgets then immediately grid/pack them. Prefer preserving this simple structure for small changes.
  - The project uses direct imports from `tkinter` (e.g., `tk`, `PhotoImage`) and plain `time.sleep` in UI callbacks — which blocks the UI. If improving UX, replace blocking sleeps with `root.after(...)` instead of threads.
  - Resource paths are relative (e.g., `imgs/Magic_eight_ball.png`). When editing image-loading code, use path checks or `os.path.join` to remain cross-platform.

- Run & debug (how humans run this project)
  - Run main app: `python src/8ball_src.py` from repo root. There is no packaging or virtualenv required; standard system Python with Tkinter is sufficient.
  - Run image test: `python src/dump.py` to verify `imgs/Magic_eight_ball.png` loads in a simple window.
  - If images fail to load, ensure you run from the repository root so `imgs/` is on the relative path, or change the code to use __file__-relative paths.

- Safety and low-risk edits
  - Small UI tweaks (labels, button text, geometry) are safe. Avoid changing global imports or introducing new heavy dependencies without user approval.
  - Avoid adding background threads without also adding synchronization and a clear reason. Prefer `tk.after` for non-blocking waits.

- Concrete examples to follow when generating code
  - To show the answer in the UI instead of printing, update the `command` of `fortune_btn` to call a short function that sets a `tk.Label`'s `text` rather than calling `print(...)`.
    - Example pattern: create a label `result_lbl = tk.Label(root, text="")` and use `result_lbl.config(text=EightBall().get_answer())` in the button callback.
  - To make the shake delay non-blocking: replace `time.sleep(2)` with `root.after(2000, set_answer)` where `set_answer` updates the label.

- Files to reference when implementing changes
  - `src/8ball_src.py` — primary edit target for UI and behavior changes. Look for `EightBall`, `shake`, `get_answer`, and `mainwindow()`.
  - `src/dump.py` — shows how `PhotoImage` is used; copy small image-handling snippets from here.

- When to ask the user
  - If a change introduces new dependencies (pip packages), ask before modifying project environment (e.g., adding `requirements.txt`).
  - If a refactor touches multiple files (e.g., introducing a package structure), propose the plan and get confirmation first.

If anything in this file is unclear or you want additional rules (testing guidance, packaging, or style rules), tell me what to add and I will iterate.