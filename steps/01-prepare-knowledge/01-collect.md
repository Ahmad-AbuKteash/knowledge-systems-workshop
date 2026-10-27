# Collect: understand the assigned source

## Concept
Collection establishes what information you have and where it came from. Here,
the trainer supplies files, so collection means inventory and provenance, not
web crawling or generating replacement content.

## Procedure
Follow WORKSHOP_MODE.md. Resolve the requested source and inspect its files.
Explain their formats and likely extraction needs. Do not transform content.
Create workspace/<source>/collected/manifest.json with source_id and a `files`
list: document_id (stable unique ID), original project-relative path, SHA-256,
byte size, and extension. Identify exact duplicate hashes, without deleting any
source. Record externally supplied provenance only when known.
Create questions.json in collected/ with 3–5 source-relevant questions, including
one clearly unsupported question. Record `id`, `question`, and `answerable` only;
do not include answers or evidence. Let the participant review question coverage.
Record collect completion in progress.json, then stop.

## Output
collected/manifest.json; collected/questions.json; progress.json.

## Participant checkpoint
Show file count, formats, duplicate groups, and the exact input folder. Can the
participant identify their assigned source and one question it should answer?
