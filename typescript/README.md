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

// Obtain a JWT access token from your dployr base server
// (see https://docs.dployr.dev/auth for details on how to authenticate with base)
const accessToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'; // issued by base

// Set the token so all requests to the instance are authenticated
tokenManager.setAccessToken(accessToken);

// Now you can make authenticated API calls to the instance
const deploymentsResponse = await client.deployments.get();
const servicesResponse = await client.services.get();

const deployments = deploymentsResponse?.deployments ?? [];
const services = servicesResponse?.services ?? [];
```

## Authentication

The SDK uses JWT-based authentication with tokens **issued by base**:

- **Access tokens** are short-lived (~10 minutes) and used for API requests to instances
- **Refresh tokens** are long-lived (24+ hours) and used to obtain new access tokens from base

Use the `TokenManager` to store and manage the tokens you receive from base. The SDK does not
auto-refresh tokens; if an access token expires you should:

1. Call your base server's refresh endpoint to get a new access token.
2. Update the SDK's token manager, e.g. `tokenManager.setAccessToken(newAccessToken)`.
3. Retry the failed request if needed.

For the full authentication flow and examples of obtaining tokens from base, see
https://docs.dployr.dev/auth.

## Client overview

`createDployrClient` returns an object with:

- `client.deployments` – list and create deployments.
- `client.services` – list services and access a single service by ID.
- `client.logs` – access log streaming.
- `client.proxy` – inspect and change proxy routes and status.
- `client.system` – read system health and info.

Each property exposes request builders generated from the OpenAPI description. Most methods
follow the pattern `get()`, `post(body)`, `delete()`, or `patch(body)`. List endpoints return
typed DTOs such as `DeploymentsGetResponse` and `ServicesGetResponse` that contain both the
items and a `total` count.

## Common operations

List deployments:

```typescript
const deploymentsResponse = await client.deployments.get({
  queryParameters: { limit: 20, offset: 0 },
});

const deployments = deploymentsResponse?.deployments ?? [];
```

List services:

```typescript
const servicesResponse = await client.services.get({
  queryParameters: { limit: 20, offset: 0 },
});

const services = servicesResponse?.services ?? [];
```

Get a single service:

```typescript
const service = await client.services.byServiceId('service-id').get();
```

Stream logs for a service or deployment (Server-Sent Events):

```typescript
const response = await client.logs.stream.get({
  queryParameters: { token: accessToken, id: 'service-or-deployment-id' },
});
// Handle the text/event-stream response using your HTTP stack.
```

Check system status:

```typescript
const status = await client.system.status.get();
```

Restart proxy:

```typescript
const result = await client.proxy.restart.post();
```

## Documentation

For full API reference and guides for the TypeScript SDK, visit
https://sdk.dployr.dev/typescript.