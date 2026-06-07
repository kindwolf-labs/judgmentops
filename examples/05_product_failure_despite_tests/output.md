# Judgment Analysis: Technical Pass, Product Fail

**Observed outcome**  
All tests provided to the agent passed. The default value in the settings store and the dispatch path now use "weekly_digest". The code change is small and locally correct.

**Why the product goal was not met (per post-launch metrics and user research)**  
- Activation rate for the new user cohort dropped 18% in the first 7 days compared to the prior "immediate" default.
- Users in the new cohort showed significantly lower engagement with core product loops that rely on timely notifications (task reminders, comment replies).
- Qualitative interviews revealed that many new users never discovered they could change the setting to "immediate" because the quieter default meant they never experienced the value of notifications.
- Unsubscribe / complaint rate improved slightly, but the business trade-off (lost activation) was worse than the original problem the team was trying to solve.

**Root judgment failures**

1. The original request was framed only as a mechanism change ("make the default quieter") rather than a product outcome ("reduce overwhelm while preserving or improving activation and perceived value of notifications").
2. Success criteria given to the agent were purely technical (default value propagated, dispatch received the expected string, tests pass). No product success criteria or leading indicators (activation, time-to-first-value, notification engagement rate) were part of the quality gate.
3. No failure memory or prior experiment data about notification defaults was consulted. A similar quiet-default experiment two years earlier had produced the same activation drop and was rolled back (recorded only in a product Notion page and a Slack thread).

**What a proper judgment layer would have required**

- Intent contract that names the real objective: "Reduce notification overwhelm for new users without regressing activation or time-to-first-core-action by more than X%."
- Quality gate that includes:
  - Primary product metrics (activation, engagement) in a controlled experiment, not only unit/integration tests.
  - Explicit measurement of the "discovery of notification value" path.
  - Review by the product owner who owns the activation metric.
- Failure memory consultation step that surfaces the prior quiet-default experiment before the new implementation begins.

**Conclusion**  
This is a canonical "technical success, business / product objective failure" case (see also JC-014 in the casebook). The agent did exactly what a narrow technical request plus passing tests asked it to do. The human judgment that should have constrained and evaluated the work was never encoded in any artifact the agent or the review process was required to consult.

**Recommended preventive rule**  
Any change to user-facing defaults that can affect activation, retention, or engagement must carry an intent contract and quality gate owned by the product manager responsible for the affected metric. "Make X quieter / faster / better" is not an acceptable intent statement. Technical tests alone are never sufficient evidence of success.
