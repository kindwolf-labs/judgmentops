A good judgment-preserving review should:
- Reference the intent contract scope and call out that "include related entities" adds joins to customer_events and billing_adjustments which may be out of scope.
- Check for required audit fields in the implementation and logs; flag if missing exported_by, export_reason, entity_count.
- Reference the failure memory (incomplete invalidation or data surface expansion leading to incidents) and require explicit column list + classification review.
- Enforce redaction: remove any internal ticket refs like FIN-4421 from code/comments/description.
- Recommend human checkpoint per policy for finance-sensitive export changes.
- Not just say "looks good, tests pass" but tie back to contract criteria and gate evidence.
- Be ready for human: structured (e.g. Scope, Audit, Data Risk, Redaction, Recommendation sections).