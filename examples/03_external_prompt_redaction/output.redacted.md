You are an expert TypeScript engineer.

Here is a simplified internal-style script that demonstrates retry logic. Your task is to turn it into a clean, self-contained public example for documentation of a hypothetical retry helper package.

```ts
// Note: The original source contained private workstation locations, project codenames,
// and credentials. Those have been replaced with clearly fake values for
// this public example. Do not use the placeholder values in real systems.

import { ExampleRetryClient } from 'example-retry-package';

const client = new ExampleRetryClient({
  endpoint: 'https://api.example.com',
  // Use a test token only. Never commit real credentials.
  token: 'test_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
});

async function runWithRetry(attemptId: string) {
  // In a real implementation you would consult your own retry policy here.
  const result = await client.executeWithRetry(attemptId);
  console.log('Retry result', result);
  return result;
}
```

Turn the above into a clean, self-contained public example for the docs site of an open-source retry helper package. Keep the structure and intent but use only public-friendly naming and clearly fictional configuration. Add a short usage note that warns readers to never hard-code credentials.
