# dispatch-scratch

Hello from Dispatch

## Contents

- `textstats.py` is a small CLI that counts lines, words and characters and lists the top words.
- `test_textstats.py` holds unit tests for it (run with `python3 -m unittest -v`).
- `docs/rendering-test.md` shows tables, task lists, code blocks, mermaid diagrams and Unicode, so you can check how Dispatch renders Markdown.

Try it:

```bash
python3 textstats.py README.md --top 3
```

## Test log

- 2026-10-06 — Dispatch greeting test
- 2026-10-06 — Screenshot test (first attempt: no screenshot received; second attempt: received IMG_0452.jpg, the Dispatch mobile Sessions view)
- 2026-10-06 — Follow-up queue test (first queued message received)
- 2026-10-06 — Follow-up queue test (second queued message received)
- 2026-10-08 — Connection test; added textstats CLI, tests, and Markdown rendering page
