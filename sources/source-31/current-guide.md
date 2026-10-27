# Nimbus integration exports and pagination

Version: 2026.2. Effective date: 2026-09-01. Owner: Integration Engineering.
Access scope: workshop-public. Supersedes previous-policy.md.

## Applicability
Nimbus order export API for direct integrations; customer workspace exit exports follow source-34.

## Creating and polling jobs
POST /v2/exports creates an asynchronous export and returns HTTP 202 with a job ID. GET /v2/exports/{job_id} returns queued, running, complete, or failed. Poll no more frequently than once every five seconds and observe the per-key export-status quota in source-05.

## Results
Completed jobs produce NDJSON files with UTF-8 encoding. Download links expire 24 hours after completion. Treat the supplied link as sensitive. An export is a point-in-time snapshot at job creation, not a live view of subsequent orders.

## Pagination and recovery
For GET /v2/orders, follow the opaque next_cursor returned by the server. Do not derive a cursor from the last order ID. Page size is at most 200. A cursor expires after 30 minutes; restart the query with the original filters and deduplicate by order ID if it expires.

## Exceptions
During the dated export maintenance notice in source-05, new jobs may return HTTP 503 while existing downloads remain available. Do not confuse that temporary condition with a permanent quota or link-lifetime change. This guide does not specify an export row-count ceiling.

Related document: operational-record.md supplements this source; read its record type and effective period before applying it.

Original synthetic workshop content. Nimbus Labs and all people, services, incidents, and rules described here are fictional. This is not legal, medical, or security advice.
