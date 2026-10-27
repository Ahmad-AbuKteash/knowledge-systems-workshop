# Nimbus incident command and recovery

Version: 2026.2. Effective date: 2026-09-01. Owner: Site Reliability Engineering.
Access scope: workshop-public. Supersedes previous-policy.md.

## Applicability
Operational incidents affecting Nimbus production services; security investigation is coordinated with source-22.

## Severity and ownership
SEV1 means widespread critical-service failure or confirmed material data integrity risk. SEV2 means substantial degradation with limited scope or a viable workaround. The on-call engineer declares an incident and assigns a commander, technical lead, and scribe. One person may temporarily fill two roles, but the commander must name the coverage.

## Response
Acknowledge the page within five minutes. If unacknowledged, page the backup on-call. The commander records impact, hypotheses, actions, and next checkpoint. Stabilize before pursuing a complete root-cause explanation. Use approved access under source-12.

## Recovery criteria
The commander may mark monitoring after mitigation and resolution after 30 continuous minutes of healthy service checks and confirmation of any affected data workflow. A restart completing successfully alone is insufficient.

## Follow-up
Complete a blameless review within five business days for SEV1 and ten for SEV2. Every action needs an owner and due date. External communication follows source-17. Support P1/P2 labels are ticket priorities, not an automatic mapping to SEV1/SEV2. No recovery-time guarantee is established here.

Related document: operational-record.md supplements this source; read its record type and effective period before applying it.

Original synthetic workshop content. Nimbus Labs and all people, services, incidents, and rules described here are fictional. This is not legal, medical, or security advice.
