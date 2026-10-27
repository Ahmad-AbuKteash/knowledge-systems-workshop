# Nimbus database migration safeguards

Version: 2026.2. Effective date: 2026-09-01. Owner: Database Engineering.
Access scope: workshop-public. Supersedes previous-policy.md.

## Applicability
Schema and large data migrations in Nimbus production relational databases, in addition to source-23 release gates.

## Plan and rehearsal
The migration request records tables, estimated rows, lock behavior, compatibility window, validation queries, and a recovery approach. Rehearse on a representative sanitized dataset. Record actual duration and load; an estimate is not a measured rehearsal.

## Expand and contract
Introduce backward-compatible schema first, deploy readers and writers that support the transition, backfill in bounded batches, and remove the old field only after old application versions are retired. Destructive changes require Database Engineering and service-owner approval.

## Operational thresholds
Use batches of at most 5,000 rows by default. Pause when replication lag exceeds 30 seconds for two consecutive checks spaced one minute apart, or when the service's declared release abort threshold is breached. Resume only after the migration lead records healthy checks and approval.

## Recovery and records
Confirm a recent verified restore point before execution. A backup is not an instant rollback plan for an incompatible application change. Record migration version, start and stop timestamps, batch progress, and validation result. This procedure does not authorize direct production access or define every database engine's locking behavior.

Related document: operational-record.md supplements this source; read its record type and effective period before applying it.

Original synthetic workshop content. Nimbus Labs and all people, services, incidents, and rules described here are fictional. This is not legal, medical, or security advice.
