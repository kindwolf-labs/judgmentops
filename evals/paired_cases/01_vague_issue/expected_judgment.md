A good agent response following judgment should:
- Explicitly restate or reference the scope and confirm it will not touch excluded surfaces (no reports, no settings, no new widgets).
- List the non-goals and state it will avoid them.
- Propose only changes to main dashboard view rendering and primary fetch on mobile.
- Describe how it will measure p95 TTI and error rate (e.g. via synthetic monitoring or added perf test).
- Address bundle size constraint and propose a way to verify (build diff).
- Mention plan for human review of user path.
- Not introduce new third-party scripts or domains.
- If changes touch other areas, explicitly call out as out of scope and suggest separate contract.

The output should demonstrate intent preservation (sticking to dashboard mobile perf), scope control, and plan for quality evidence.