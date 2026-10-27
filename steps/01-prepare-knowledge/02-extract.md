# Extract: convert content into readable text

## Prerequisite
collect complete; manifest hashes match original files.

## Concept
Extraction reads source content. It should preserve facts before cleaning begins.

## Procedure
Read WORKSHOP_MODE.md. Explain converter choice per file. Copy UTF-8 Markdown/text
content as text; use MarkItDown.convert_local for HTML and supported binary formats.
Use the project .venv. Install requirements-formats.txt only if PDF/Office inputs
need those extras. Do not add OCR or Docker automatically for image-only PDFs;
report the blocker and ask for trainer-provided extracted text.
Write a repeatable helper under workspace/<source>/scripts/ if useful. Preserve
input extensions in output names to avoid same-stem collisions. Create readable
Markdown and extracted/documents.json matching the common record contract.
Keep navigation and repeated text for the next step. Report empty/failed
extractions explicitly; partial extraction is not a completed stage. Compare
representative facts/tables against originals and show examples. Update progress.

## Output
extracted/*.md; extracted/documents.json; a conversion report.

## Participant checkpoint
Open one original and its Markdown. Are numbers, table relationships, headings,
and qualifications preserved? A nonempty output alone is insufficient.
