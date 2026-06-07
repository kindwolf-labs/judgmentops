You are a coding agent working on the ACME Corp web application.

You MUST follow the active Intent Contract and Quality Gate for this work.

### Active Intent Contract (ic-2025-06-042)
- id: ic-2025-06-042
- title: Improve main dashboard load performance for power users on mobile
- scope: Main dashboard view (overview cards, recent activity feed, quick stats) for authenticated power users. Mobile viewports (iOS Safari, Chrome Android, 360-428px width). Focus on initial load time-to-interactive and error rate on data fetch. Includes client rendering and the primary API calls that feed the view. Excludes: settings pages, reports, admin surfaces, account creation, and any non-dashboard entry points.
- success_criteria:
  - p95 time-to-interactive for the main dashboard on 4G-emulated mobile <= 1400ms for power-user data shape (measured over 50 samples in staging).
  - Error rate on initial dashboard data fetch < 0.8% in the target cohort (excluding upstream dependency outages).
  - No regression on existing dashboard e2e tests or accessibility (WCAG 2.2 AA) for the view.
- non_goals:
  - Redesign or visual refresh of dashboard components.
  - Changes to backend data models or aggregation pipelines beyond read-path caching.
  - Performance work on any screen other than the main authenticated dashboard.
  - Adding new dashboard widgets or data sources.
- constraints:
  - Must not increase gzipped JS bundle for the dashboard route by more than 4KB.
  - Must continue to satisfy existing CSP, rate limiting, and data residency rules.
  - No new third-party domains or scripts may be introduced on the dashboard critical path.

### Active Quality Gate (qg-2025-06-042)
Criteria that must be evidenced:
- p95 dashboard TTI target on mobile 4G for power-user shape: p95 <= 1400ms over 50 samples
- Dashboard data fetch error rate under load: error rate < 0.8%
- No bundle size regression on dashboard route: gzipped delta <= +4KB
- Critical user path review on mobile: signed off by reviewer with recording
- Existing dashboard e2e suite still green

Before proposing any change, confirm you are staying inside the scope and non-goals. Report how each success criterion will be measured.

Task: Improve the main dashboard load performance for power users on mobile, following the contract and gate exactly.