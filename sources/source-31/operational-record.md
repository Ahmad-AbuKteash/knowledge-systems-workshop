# Integration handoff: restart after cursor expiry

Record version: 1.0. Owner: Integration Engineering. Access scope: workshop-public.
Record type: email.

Published: 2026-10-25. Case date: 2026-10-24. Record type: fictional integration email.
The Nimbus order sync paused for 42 minutes after receiving a page. The saved cursor is now rejected as expired. Keep the original query filters, restart pagination, and use order IDs to avoid inserting already processed orders twice. Do not construct a replacement cursor from the last order's timestamp. A new export job would represent a new snapshot and should not silently be merged as if it had the earlier job's creation time. The record provides recovery context, not a production authorization.

## Relationship to policy
Read alongside current-guide.md. This record supplements the collection and does not supersede the full policy. Case records, exercises, and proposals describe their stated context; they are not general policy changes.

Original synthetic workshop content. Nimbus Labs and all people, services, incidents, and rules described here are fictional. This is not legal, medical, or security advice.
