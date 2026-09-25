## Memory update protocol

AFTER each real turn:

1. Append the turn to `last_5_turns`; drop older turns.
2. Extract only explicit facts from the actual conversation.
3. Update topic list only when the topic was actually discussed.
4. Add an inside joke only after an actual shared reference repeats or is clearly established.
5. Add a boundary only when explicitly stated or directly evidenced.
6. Update the 5 ledger counters from observable behavior.
7. Record repeated pattern only after the interaction pattern occurs at least twice.
8. Update `last_state` from the current episode.
9. Record outcome only from observed follow-up, never from imagined success/failure.
10. Never write AI-generated candidate text as fact.
11. Never write inferred attraction, rejection, attachment style, or intent as fact.
12. Preserve source provenance for imported screenshots/cases.
