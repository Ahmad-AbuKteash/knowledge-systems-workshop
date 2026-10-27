# Nimbus database migration safeguards - historical

Version: 2025.1. Effective date: 2025-01-01. Owner: Database Engineering.
Access scope: workshop-public. Status: historical.
Superseded on 2026-09-01 by current-guide.md.

## Historical scope
Schema and large data migrations in Nimbus production relational databases, in addition to source-23 release gates.

## Terms before 2026-09-01
Default batches were at most 20,000 rows. Replication lag triggered a pause above 60 seconds on one check.

Only the historical terms stated here are preserved in this excerpt. Do not infer additional historical rules from the current document. For events on or after 2026-09-01, consult current-guide.md and any applicable notices.

Original synthetic workshop content. Nimbus Labs and all people, services, incidents, and rules described here are fictional. This is not legal, medical, or security advice.
