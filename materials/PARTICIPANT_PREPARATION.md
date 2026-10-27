# Engineering Knowledge Systems for AI Agents

> Archived preparation guide from the earlier lab-based version. Use the
> [current participant preparation guide](../PREPARATION.md) for this project.

## Participant preparation guide

Complete setup at least **one day before the workshop**. Use any AI coding environment with local file and terminal access. Windows and macOS are supported.

**Core tools:** Python, Git, and Microsoft MarkItDown. **No Docker, Docling, OCR engine, vector database, GPU, or local AI model download is required.** Docling and hybrid search are optional trainer demonstrations.

## 1. What you need

- Laptop, charger, stable internet, and permission to install developer tools.
- An AI coding environment installed and signed in, with local command execution enabled. Examples include Codex, Claude Code, Cursor, or an editor with an agent. A chat-only interface cannot perform local setup.
- Account access and sufficient usage/credits for your chosen tool. Check your provider's billing requirements.
- Free disk space for Python and packages. Allow a few GB as a preparation allowance.

Reserve **30–45 minutes** for installation and checks; actual time varies. If you use a managed laptop, arrange installation permission with IT first.

## 2. Open the workshop folder

The trainer will send a repository URL or project archive before the workshop. No remote URL has been published yet.

1. Download the project archive and extract it, or clone the supplied repository URL.
2. Open the resulting `ai-knowledge-systems` folder in your preferred AI coding environment. For terminal agents, launch the agent from this folder.
3. Confirm you can see `README.md`, `requirements.txt`, `scripts/`, `labs/`, and `data/`.
4. Enable local file and terminal access in your agent's settings if needed.

If you received only this guide, complete sign-in and tool access now, then return when the project files arrive. The checks below depend on files in this repository.

## 3. Ask your AI to prepare the project

Paste the following prompt. Your assistant should perform the setup and report actual results, rather than only suggest commands.

```text
Prepare this project for "Engineering Knowledge Systems for AI Agents".

Read AGENTS.md, README.md, requirements.txt, and labs/00-setup/README.md first.
Work in this project folder. Perform the setup with local file/terminal tools,
explaining each major step. Use official documentation where needed. If you
cannot execute commands, tell me and give exact manual instructions for my OS.

1. Inspect the OS, CPU architecture, current folder, and installed tools.
2. Check Git and install it if missing using an official supported method.
   Verify git --version. Do not configure a remote or publish anything.
3. Check uv; install it from Astral's official instructions if needed. Use
   Python 3.12 if available, or a compatible existing 3.13/3.14 installation.
   Do not replace system Python. If needed, let uv install Python 3.12.
4. Create .venv in this project. Inspect and reuse a compatible existing
   environment; do not delete it automatically.
5. Install requirements.txt in .venv. The core converter is MarkItDown with
   PDF, DOCX, and XLSX extras. Do not install Docling or optional extensions.
6. Run scripts/doctor.py using the .venv Python and inspect its real output.
7. Run scripts/convert.py on the bundled sample inputs. If outputs already
   exist, preserve them and use a new output folder instead of overwriting.
8. Inspect the generated Markdown. Confirm that the current expense policy
   retains USD 85, the historical policy USD 60, and the runbook the P1 rule.
   Read the generated manifest and check source filenames are traceable.
9. If a PDF smoke test is needed, create a small synthetic PDF with a local
   helper dependency in .venv, convert it, and check the actual extracted text.
   Report HTML/Markdown, PDF, and Office checks separately; do not claim a
   format passed unless tested. Scanned PDFs/OCR are optional, not a blocker.
10. Save outputs/setup-report.md with OS/architecture, tool versions, commands
    run, passed/failed checks, and any action required before the workshop.
11. Explain how to reopen the folder and rerun doctor.py on my OS.

Do not complete later labs, create cleaned knowledge, or read the instructor
answer key. Do not install Docker, WSL, a vector database, embedding models,
or a particular editor. Do not restart or modify existing Docker containers.
Preserve source documents and existing projects. Request permissions required
by your environment and respect company policy. Do not disable certificate
verification or include credentials in reports. Use only synthetic local files.

Official references:
https://github.com/microsoft/markitdown
https://docs.astral.sh/uv/getting-started/installation/
https://docs.astral.sh/uv/guides/install-python/
https://git-scm.com/downloads

Finish with what you actually verified and what remains untested.
```

Approve appropriate setup requests, complete any installer dialogs, then ask your assistant to continue. If a new command is not found, reopen the terminal and AI environment to refresh PATH.

## 4. Review your setup

Send this follow-up:

```text
Review outputs/setup-report.md against actual command results. Show me one
converted document and its source entry in the manifest. Confirm no later lab
was completed. Explain any failures and the smallest next step to fix them.
```

The bundled mini dataset contains two synthetic expense policies and one on-call runbook. It checks that conversion works; it is not the full mixed-format workshop corpus. The trainer will provide curated samples separately as they are prepared.

## 5. Manual commands if needed

Run from the project root. Python 3.12 is recommended; this setup accepts 3.12–3.14. If uv is missing, ask your AI to install it using the official link above. uv can download Python when creating the environment.

### Windows — PowerShell

Open Start, search **PowerShell**, and open it. Navigate to the extracted project folder; your AI can give you the exact `Set-Location` command for its location. Then run one line at a time:

```powershell
uv venv --python 3.12 .venv
uv pip install --python .\.venv\Scripts\python.exe -r requirements.txt
.\.venv\Scripts\python.exe scripts/doctor.py
.\.venv\Scripts\python.exe scripts/convert.py
Get-Content .\data\extracted\expense-policy-2026.html.md
```

### macOS — Terminal

Open Spotlight with Command + Space, search **Terminal**, and open it. Navigate to the extracted project folder; your AI can provide the exact `cd` command. Then run one line at a time:

```bash
uv venv --python 3.12 .venv
uv pip install --python ./.venv/bin/python -r requirements.txt
./.venv/bin/python scripts/doctor.py
./.venv/bin/python scripts/convert.py
cat data/extracted/expense-policy-2026.html.md
```

Create `.venv` once; do not recreate it each session. Explicit executable paths avoid environment activation and PowerShell policy changes. If extraction already exists, pass a fresh `--output` folder to convert.py; it refuses overwrites by default.

**Success:** doctor exits successfully, conversion reports three successful files, the current policy output contains USD 85, and `data/extracted/manifest.json` records the source mapping. These commands do not test PDF or Office formats on their own.

## 6. Troubleshooting

Ask your AI:

```text
Diagnose the last error using actual output and official documentation. Try
the smallest appropriate fix while preserving working setup. If permissions,
network policy, billing, or package compatibility block progress, explain
exactly what help is needed rather than retrying indefinitely.
```

- **Missing command:** reopen the terminal/editor and ask the assistant to check PATH.
- **Wrong Python:** use the explicit .venv executable and inspect its version.
- **Blocked installation:** contact IT with the specific tool or host in the error; do not disable security controls.
- **Conversion failure:** share the filename, command, and error with the trainer. Image-only PDFs may require OCR outside the core exercise.
- **AI unavailable:** check sign-in, entitlement, billing, and usage with your provider.

Send the trainer your OS/chip, failed command, error text, and setup report. Remove credentials and personal information first.

## 7. Ready for the workshop

- [ ] My AI environment responds and can run commands in the project.
- [ ] Git and a compatible Python are available.
- [ ] Project dependencies are installed in .venv.
- [ ] scripts/doctor.py passes.
- [ ] Bundled sample conversion passes and I inspected the Markdown.
- [ ] I reviewed outputs/setup-report.md and reported unresolved failures.
- [ ] I have the latest project files and my laptop charger.

Keep original files in data/raw unchanged. We will create prepared knowledge during the workshop. Do not use private company documents: content read by your AI agent may be sent to its model provider.
