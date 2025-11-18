# @dployr-io/dployr-sdk

TypeScript SDK for interacting with [dployr](https://github.com/dployr-io/dployr).

## Installation

```bash
npm install @dployr-io/dployr-sdk
# or
pnpm add @dployr-io/dployr-sdk
# or
yarn add @dployr-io/dployr-sdk
```

## Usage

```typescript
import { createDployrClient } from '@dployr-io/dployr-sdk';

// Connect to your Dployr instance
const { client, tokenManager } = createDployrClient('https://your-dployr-instance.com');

// Login to get authentication tokens
const auth = await client.auth.request.post({
  email: 'user@example.com'
});

// Store tokens for authenticated requests
tokenManager.setTokens(auth.access_token, auth.refresh_token);

// Now you can make authenticated API calls
const deployments = await client.deployments.get();
const services = await client.services.get();
```

## Authentication

The SDK uses JWT-based authentication with access and refresh tokens:

- **Access tokens** are short-lived (~10 minutes) and used for API requests
- **Refresh tokens** are long-lived (24+ hours) and used to obtain new access tokens

Use the `TokenManager` to store and manage your tokens after login.

## Documentation

For full API reference and guides, visit [dployr docs](https://docs.dployr.dev).