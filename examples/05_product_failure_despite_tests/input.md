# Task

Implement a "smart default" for the new in-app notification frequency setting.

Current behavior: new users receive "immediate" notifications for everything by default.

Requested change: switch the default to a quieter setting so users are not overwhelmed.

The team provided:
- The settings UI component
- The notification dispatch service interface
- A set of unit tests that assert the default value is used when no preference is stored
- An integration test that creates a user and asserts that the dispatch service receives "weekly_digest" for the new default

All provided tests pass after the change. The PR description says "Default is now quieter as requested. Tests green."