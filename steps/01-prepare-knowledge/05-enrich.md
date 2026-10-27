# Enrich: attach document metadata

## Prerequisite
structure complete.

## Concept
Metadata describes authority, applicability, and provenance. It does not create
facts absent from the source or enforce access permissions by itself.

## Procedure
Follow WORKSHOP_MODE.md. Add a metadata object to each eligible document with:
title, version, effective_date, supersedes, owner, access_scope. Use null for
unknown values. Resolve supersedes to another document_id only with evidence.
Do not infer policy status from an apparent year in the filename alone.
Retain source_id, document_id, source_file, source_sha256, and text at top level.
Write knowledge/documents.json and readable Markdown files with metadata displayed
separately. Create knowledge/index.md listing documents and their original sources.
Explain one filled field and one unknown field. Update progress and stop.

## Output
knowledge/documents.json; readable documents; knowledge/index.md.

## Participant checkpoint
Which source supports each metadata value? Can current and historical policies
be distinguished without discarding either?
