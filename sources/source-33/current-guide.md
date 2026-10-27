# Nimbus customer roles and administrator recovery

Version: 2026.2. Effective date: 2026-09-01. Owner: Customer Identity.
Access scope: workshop-public. Supersedes previous-policy.md.

## Applicability
Nimbus customer workspace permissions; these roles are distinct from Nimbus employee privileges in source-12.

## Role capabilities
| Role | Capabilities |
|---|---|
| Viewer | Read permitted workspace records |
| Editor | Viewer actions plus create and update business records |
| Administrator | Editor actions plus users, API keys, billing, and export requests |

## Membership
Administrators invite named individuals and assign the least role needed. Guests must have an expiry no later than 30 calendar days after invitation. Role changes take effect on the next authorization check; an open browser page is not proof of continuing permission.

## Administrator safeguards
Keep at least two active administrators when possible. The final administrator cannot remove their own administrator role through self-service. If no administrator is available, Support opens a recovery case and verifies organizational authority through approved evidence and an existing verified channel.

## Boundaries
A billing contact is not automatically a workspace administrator. A screenshot of an invoice alone is insufficient to transfer ownership. Support cannot reveal recovery secrets or bypass verification because a request is urgent. Customer exports use source-34; workforce emergency access does not grant customer administrator status.

Related document: operational-record.md supplements this source; read its record type and effective period before applying it.

Original synthetic workshop content. Nimbus Labs and all people, services, incidents, and rules described here are fictional. This is not legal, medical, or security advice.
