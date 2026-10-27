# Nimbus webhook signatures and event replay

Version: 2026.2. Effective date: 2026-09-01. Owner: Developer Platform.
Access scope: workshop-public. Supersedes previous-policy.md.

## Applicability
Nimbus production order-event webhooks; delivery timing is defined in source-02/webhooks.md.

## Verification
Nimbus signs the exact raw request body with HMAC-SHA256 using the endpoint signing secret. The Nimbus-Signature header contains a hexadecimal digest; Nimbus-Timestamp contains Unix seconds. Receivers reject timestamps more than 300 seconds from their trusted clock and compare digests using a constant-time comparison.

## Acknowledgment and duplicates
After verification, persist the event ID before acknowledging HTTP 2xx. Acknowledge within the ten-second deadline in source-02. Delivery is at least once; event ID, not payload text, is the deduplication key. Retry deliveries keep the original event ID.

## Rotation and replay
During a planned secret rotation, old and new secrets overlap for 24 hours. Verify against either registered active secret during that interval. Operators can request a replay of events created within the previous seven calendar days; a replay retains the original event ID but receives a fresh timestamp and signature.

## Boundaries
Replay availability is not a general data-retention promise. This document contains no real signing secret and does not prescribe a programming-language SDK. Incident-driven revocation can end an overlap immediately under Security direction.

Related document: operational-record.md supplements this source; read its record type and effective period before applying it.

Original synthetic workshop content. Nimbus Labs and all people, services, incidents, and rules described here are fictional. This is not legal, medical, or security advice.
