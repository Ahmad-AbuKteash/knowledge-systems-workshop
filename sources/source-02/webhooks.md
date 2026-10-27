# Nimbus webhook delivery

Version: 1.0. Effective date: 2026-02-01. Owner: API team.
Access scope: workshop-public.

Webhook receivers must respond with HTTP 2xx within 10 seconds.
Failed deliveries are retried at 1 minute, 5 minutes, and 30 minutes.
Use the event ID to deduplicate deliveries. Delivery is at least once.
This document does not specify data-retention duration.

Original synthetic workshop content. Nimbus Labs is fictional.
