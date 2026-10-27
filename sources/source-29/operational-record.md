# Receiver incident: body reserialization

Record version: 1.0. Owner: Developer Platform. Access scope: workshop-public.
Record type: case-record.

Published: 2026-10-11. Case date: 2026-10-10. Record type: fictional integration investigation.
A Nimbus customer's webhook receiver parsed JSON and serialized it again before calculating the signature. Whitespace changed, so verification failed although the event fields appeared identical. The receiver was corrected to retain the original raw bytes. The team also found that retry deliveries had been inserted as new events instead of deduplicated by event ID. This case does not justify disabling timestamp checks or accepting unsigned deliveries. No secret, customer name, or executable exploit is included.

## Relationship to policy
Read alongside current-guide.md. This record supplements the collection and does not supersede the full policy. Case records, exercises, and proposals describe their stated context; they are not general policy changes.

Original synthetic workshop content. Nimbus Labs and all people, services, incidents, and rules described here are fictional. This is not legal, medical, or security advice.
