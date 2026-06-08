# Submission Run - 2026-06-09

## Scope

This run attempted to advance JudgmentOps through three official startup or cloud program application flows:

1. AWS Activate / AWS Startups.
2. Microsoft for Startups Founders Hub.
3. Google for Startups Cloud Program.

No application was submitted. No cold email or support request was sent.

Run timestamp: `2026-06-09 00:42:35 +08:00`

Applicant identity prepared for use:

- Name: Y. Luo
- Role: Project Lead / Founder
- Project: JudgmentOps
- Website: https://github.com/kindwolf-labs/judgmentops

## AWS Activate

- Official starting URL: https://aws.amazon.com/startups/credits/
- Selected route: Activate Founders, for a bootstrapped or self-funded startup.
- Application URL reached: https://aws.amazon.com/startups/join?destination=/credits/apply
- Status: `BLOCKED_AT_HUMAN_CHECKPOINT`
- Checkpoint: AWS Builder ID sign-in or sign-up.
- Page instruction: create or sign in with an AWS Builder ID before accessing the credit application.
- Fields entered: none.
- Submission performed: no.
- Confirmation ID: none.
- Evidence: `docs/submission_evidence/2026-06-09/aws_activate_login_checkpoint.png`

The official page states that Activate Founders is the direct route for bootstrapped or self-funded applicants. Later steps also require a paid-tier AWS account to be linked before submission.

## Microsoft For Startups

- Official starting URL: https://startups.microsoft.com/
- Application URL attempted: https://foundershub.startups.microsoft.com/apply
- Redirect reached: Microsoft Azure account sign-in at `login.microsoftonline.com`.
- Status: `BLOCKED_AT_HUMAN_CHECKPOINT`
- Checkpoint: Microsoft account sign-in.
- Page instruction: sign in to continue to Microsoft Azure.
- Fields entered: none.
- Submission performed: no.
- Confirmation ID: none.
- Evidence: `docs/submission_evidence/2026-06-09/microsoft_founders_hub_login_checkpoint.png` (account identifier redacted)

The user must choose the appropriate Microsoft account and complete any identity or account verification before the application form can be inspected or filled.

## Google For Startups Cloud

- Official starting URL: https://cloud.google.com/startup
- Application URL attempted: https://cloud.google.com/startup/apply
- Selected route: Google for Startups Cloud Program; final tier still requires eligibility confirmation.
- Status: `FAILED`
- Blocker: the application URL first returned `ERR_CONNECTION_CLOSED`, then the in-app browser security policy blocked further access to that URL.
- Fields entered: none.
- Submission performed: no.
- Confirmation ID: none.
- Screenshot: unavailable because the application page could not be opened.

The official landing page was successfully verified and exposed the application link. The user should open the application URL directly in a normal browser session, then select the truthful pre-funded, early-stage, or AI startup route based on project identity, funding, region, prior credits, and account status.

## Outcome

| Target | Outcome | Deepest verified point |
| --- | --- | --- |
| AWS | Blocked at human checkpoint | AWS Builder ID sign-in or sign-up |
| Microsoft | Blocked at human checkpoint | Microsoft Azure account sign-in |
| Google | Failed in current browser environment | Official landing page verified; application URL blocked |

The success criterion of advancing three official flows was met at the route-verification level, but none reached a submit-ready review screen.
