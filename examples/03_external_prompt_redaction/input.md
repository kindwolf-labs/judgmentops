You are an expert TypeScript engineer.

Here is an internal debugging script we use in production:

```ts
// /private/example/path/services/billing/src/debug/retry-debug.ts
import { InternalBillingClient } from '@example-internal/billing-client';
import { ACME_RETRY_STRATEGY } from '../config/secrets';

const client = new InternalBillingClient({
  endpoint: 'https://billing-orchestrator-v2.private.example',
  token: 'FAKE_TOKEN_DO_NOT_USE_9f8e7d6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a1f0e'
});

async function debugRetry(attemptId: string) {
  // See incident INC-4421 and the agent trace from 2025-04-02
  const result = await client.retryWithStrategy(attemptId, ACME_RETRY_STRATEGY);
  console.log('Internal retry result for secret-project-xyz', result);
  return result;
}
```

Turn this into a clean, self-contained public example for our open-source docs site showing how to use a hypothetical `example-retry` package. Keep the logic but make it suitable for external developers. Do not mention any internal tools.