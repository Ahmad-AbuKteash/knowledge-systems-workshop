# Index: store searchable knowledge locally

## Prerequisite
embed complete; embeddings match current records and validated knowledge.

## Concept
The local SQLite store keeps text, metadata, and vectors together. Our small
workshop corpus uses exact cosine comparison at query time, not an approximate
nearest-neighbor index or a database server.

## Procedure
Follow WORKSHOP_MODE.md. Invoke tools/retrieval.py index <source> with .venv Python.
The helper checks record hashes, identities, dimensions, finite vectors, and
configuration consistency, then creates index/knowledge.sqlite3. It refuses an
existing database; follow the shared history rules for deliberate reruns.
Inspect row count and one record's source/version. Explain what SQLite stores
and that similarity ranking will be computed during retrieval. No API call is
needed for this step. Update progress and stop.

## Output
index/knowledge.sqlite3 with records and index configuration/provenance.

## Participant checkpoint
Do stored records match the embedded chunks? Can the database be reopened?
Does each record retain enough evidence to cite the original document?
