# Judgment-Based PR Review Gate — PR #4912 (Bulk Export on Transactions)

**Active Intent Contract reference:** ic-2025-05-019 (Finance bulk operations — limited to read-only exports of transaction data with explicit consent and audit logging. Non-goals include any write-path changes, new PII export surfaces, or changes to retention policy.)

## Scope Check
- Change is mostly within declared scope (transactions table export).
- However, the new "include related entities" checkbox pulls in data from the `customer_events` and `billing_adjustments` tables via a new JOIN that was not part of the original contract.
- This is a scope expansion. Requires either contract amendment or explicit waiver.

## Quality Gate Status (qg-2025-05-019)
- CSV generation performance: no p95 measurement provided for the new path with "include related entities" on large accounts. Existing benchmark only covers the old simple export.
- Audit logging: the PR adds a log line but does not include the required `exported_by`, `export_reason`, and `entity_count` fields mandated by the contract.
- Consent / data classification: the new related-entities path includes fields classified as "finance-sensitive" that are not covered by the current export consent banner. Redaction gate (below) flagged this.

## Redaction Gate
- No private workstation locations or tokens detected in the diff or PR description.
- One comment in the code still references an internal ticket `FIN-4421` (internal-only). Must be removed before merge.

## Failure Memory Hits
- fm-2024-12-007: Previous export feature added a "convenience" join that later caused a data incident because the joined table contained unredacted PII for a subset of records.
- Preventive rule from that memory: "Any export that crosses table boundaries must explicitly list the columns and data classes being exported and must be reviewed against current data classification."

## Recommendation
**Block merge** until the following are resolved:

1. Either amend ic-2025-05-019 to explicitly authorize the related-entities join, or remove the checkbox for this PR.
2. Add performance evidence (or a quality gate waiver) for the bulk path with large related-entity sets.
3. Update audit logging to the exact fields required by the contract.
4. Remove internal ticket reference and re-run redaction gate.
5. Product owner sign-off that the expanded data surface is acceptable under current consent and classification rules.

**Human checkpoint required** (per hac-2025-05-003 for any export surface change touching finance-sensitive data).

If the above are addressed, this change can proceed with low residual judgment risk. As written, it repeats a documented failure class.
