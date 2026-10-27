# Trainer checklist

## Before sharing
- Assign one source per participant or pair; sources contain only input files.
- Rehearse all eleven commands using the actual supported clients and OS versions.
- Samples included are original synthetic content. For added public material,
  record provenance/reuse terms in trainer records and verify extraction quality.
- Keep the expected answers and evidence outside the participant repository.
- Verify your OpenAI project can call text-embedding-3-small with 512 dimensions.
  Distribute keys privately, use appropriate project restrictions, monitor actual
  spend, and revoke workshop credentials afterwards. Do not assume a budget alert
  guarantees a hard spending cap.
- Prepare compatible per-source recovery snapshots after each stage; do not ship
  fake completed outputs. Record hashes, package versions, and actual checks.
- Confirm that API data transfer is appropriate for every assigned source.
- Publish the repo/archive and send PREPARATION.md with its URL.

## During the workshop
Explain one concept, demonstrate one command, then let participants invoke it.
Insist on visible outputs and inspection checklists. Do not chain the entire
pipeline. Stage 1 prepares knowledge; Stage 2 embeds/indexes/tests that knowledge.
Embedding and query actions use the provided key; local indexing does not.

## Recovery
If a prerequisite fails, fix or restore that stage only. Have participants copy a
verified recovery snapshot into their own workspace, then recheck hashes and
progress. Do not claim that manually marked progress validates its artifacts.

## Completion
Review actual retrieved evidence and one grounded answer. An unsupported question
should produce an abstention even when similarity search returns candidates.
Conceptual slides remain in materials/. The old workshop deck is reference
material and must be adapted before reuse with this command-driven structure.
