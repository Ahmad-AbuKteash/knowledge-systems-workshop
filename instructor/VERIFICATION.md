# Build verification

Checked on Windows on 2026-10-27 with Python 3.13.15 and SQLite 3.50.4.

- Installed the core requirements in the project virtual environment.
- `pip check` reported no broken requirements.
- `tools/doctor.py` passed HTML extraction, preserving the sample USD 85 value.
- Installed versions: MarkItDown 0.1.9, OpenAI SDK 2.54.0, python-dotenv 1.2.4.
- Seven offline retrieval helper tests passed. API responses and vectors in
  these tests are synthetic fixtures; these are not retrieval quality results.
- All eleven Codex skills passed the Skill Creator validator.
- Claude and Copilot adapter frontmatter passed structural checks.
- `tools/sync_commands.py --check` confirmed adapters match their generator.
- Source folders contain no README files. Participant workspace contains only
  its placeholder; no participant exercises were completed.
- Git ignores `.env` and participant output paths.

Before delivery, rehearse native command discovery in each supported AI client,
installation on macOS, and a complete source workflow using a configured OpenAI
key. No live API calls, authentication checks, or paid embeddings were performed
during this build. Optional PDF/DOCX/XLSX extraction was not tested here.
