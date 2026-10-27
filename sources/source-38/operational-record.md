# ADR-NIM-042: export queue isolation

Record version: 1.0. Owner: Architecture Council. Access scope: workshop-public.
Record type: decision-record.

Published: 2026-10-23. Decision date: 2026-10-23. Status: proposed. Owner: Nimbus Export Platform.
Context: the October 21 eu-central export incident motivated evaluation of isolating export workers from interactive order traffic. Proposed decision: dedicate a worker pool to export jobs. Alternatives: shared pool with stricter scheduling, or a separate regional queue. Expected benefit: reduced contention. Costs and operational overhead remain estimates; no benchmark has been completed. The Architecture Council has not accepted the proposal. This record does not prove the incident's root cause or authorize deployment. Source-24 contains the historical incident timeline.

## Relationship to policy
Read alongside current-guide.md. This record supplements the collection and does not supersede the full policy. Case records, exercises, and proposals describe their stated context; they are not general policy changes.

Original synthetic workshop content. Nimbus Labs and all people, services, incidents, and rules described here are fictional. This is not legal, medical, or security advice.
