# Engineering Knowledge Systems for AI Agents

An instructor-led workshop: one assigned source, one manually requested step at
a time, with your AI agent explaining its work in your own session.

Repository name: **knowledge-systems-workshop**. Participants clone this repository
only. The instructor's React/Java demo is a separate private repository named
**xperience-knowledge-app**.

## Start

1. Clone/download this project and follow [PREPARATION.md](PREPARATION.md).
2. Get your source assignment from the trainer.
3. Open the project root in Claude Code, Codex, or VS Code with Copilot.
4. Invoke only the step the trainer introduces. Inspect the output before moving on.

## Commands

| Step | Claude Code / Copilot prompt | Codex skill |
|---|---|---|
| Collect | `/collect source-01` | `$collect source-01` |
| Extract | `/extract source-01` | `$extract source-01` |
| Clean | `/clean source-01` | `$clean source-01` |
| Structure | `/structure source-01` | `$structure source-01` |
| Enrich | `/enrich source-01` | `$enrich source-01` |
| Validate | `/validate source-01` | `$validate source-01` |
| Chunk | `/chunk source-01` | `$chunk source-01` |
| Carry metadata | `/carry-metadata source-01` | `$carry-metadata source-01` |
| Embed | `/embed source-01` | `$embed source-01` |
| Store/index | `/index source-01` | `$index source-01` |
| Test retrieval | `/test-retrieval source-01` | `$test-retrieval source-01` |

Replace source-01 with YOUR assignment. VS Code here means Copilot prompt files
in a supported Local/agent session; other extensions use their own invocation.
Reload your session after cloning so commands are discovered. If a command does
not appear, ask the agent to read WORKSHOP_MODE.md and the exact step guide, then
perform only that guide for your source. This fallback uses the same procedure.

## Two stages

```text
steps/
  01-prepare-knowledge/
    01-collect.md
    02-extract.md
    03-clean.md
    04-structure.md
    05-enrich.md
    06-validate.md
  02-build-retrieval-index/
    01-chunk.md
    02-carry-metadata.md
    03-generate-embeddings.md
    04-store-and-index.md
    05-test-retrieval.md
```

Each guide defines purpose, procedure, output, and inspection checkpoint. Skills
and prompt files are thin adapters; procedures are maintained only in steps/.
[WORKSHOP_MODE.md](WORKSHOP_MODE.md) defines explanations, progress, and reruns.

## Sources and participant work

Sources contain input files only—no source READMEs. Three original synthetic
sample collections are included for rehearsal and can be replaced or extended
with approved inputs before delivery:

| Folder | Topic | Intentional challenges |
|---|---|---|
| sources/source-01 | Employee policies | Historical/current policy, HTML navigation, leave table |
| sources/source-02 | API documentation | Changed rate limit, exact identifiers, retry conditions |
| sources/source-03 | Customer support | Changed refund window, exceptions, response targets |

These are fictional teaching documents, not public company policies. Participants
work in their own clone; local workspace/ is ignored by Git. Do not modify sources/.

After all steps, export reviewed results to the tracked `submissions/<source>/`
folder and commit only that source's submission. Follow [CONTRIBUTING.md](CONTRIBUTING.md)
for branches, export, commit, push, and instructor collection.

```text
workspace/source-01/
  collected/    extracted/    cleaned/       structured/
  knowledge/    chunks/       embeddings/    index/
  evaluation/   scripts/      history/       progress.json
```

## Common stack

- Python 3.12–3.14 and MarkItDown for extraction.
- OpenAI `text-embedding-3-small`, explicitly set to 512 dimensions.
- SQLite (included with Python) to store records, metadata, and vectors.
- Exact cosine search over the small local corpus; no ANN extension/server.
- The participant's existing agent reads returned passages and generates answers.

OpenAI calls send chunk/query text externally and use API credits. Stage 1 and
local indexing need no key. `/embed` and `/test-retrieval` do. The helper checks
current artifact hashes and refuses stale or mismatched embeddings/indexes.

## Supporting files

- [Preparation](PREPARATION.md): Windows/macOS setup, API key handling.
- [Trainer checklist](instructor/CHECKLIST.md): assignment, rehearsal, recovery.
- [Concept slides](materials/knowledge-base-and-rag.md): knowledge bases and RAG.
- [Workshop presentation](materials/workshop-slides.md): concepts, practical steps, and illustration descriptions.
- `workshop.json`: command routing and shared retrieval configuration.
- `tools/`: readiness check, embedding/index/search helpers, adapter generation.
- `tests/`: offline helper checks using clearly synthetic vectors; no API calls.

After changing command routing, run `python tools/sync_commands.py`. Verify with
`python tools/sync_commands.py --check`. Native skill/prompt discovery should be
rehearsed in each target environment before the event.

Repository: https://github.com/RamiY123/knowledge-systems-workshop

The repository is initially private. Grant participants access before cloning,
and create the workshop branch when ready. Distribute API keys separately;
do not include keys or private answer keys in this repository.
