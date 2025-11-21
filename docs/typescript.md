---
outline: deep
---

# TypeScript SDK

## Installation

```bash
npm install @dployr-io/dployr-sdk
# or
pnpm add @dployr-io/dployr-sdk
# or
yarn add @dployr-io/dployr-sdk
```

## Creating a client

```ts
import { createDployrClient } from "@dployr-io/dployr-sdk";

// Point this at your instance address
const { client, tokenManager } = createDployrClient("https://your-instance.example.com");
```

The factory returns:

- `client`: generated `DployrClient` bound to your base URL
- `tokenManager`: helper object storing JWTs

For the JSON shapes used in request bodies and responses, see
the [request and response shapes](/reference) page.

## Authentication

Dployr instances expect a bearer token in the `Authorization` header.

```ts
// After obtaining tokens from base
const accessToken = "ACCESS_TOKEN_FROM_BASE";
const refreshToken = "REFRESH_TOKEN_FROM_BASE";

tokenManager.setTokens(accessToken, refreshToken);
```

All subsequent requests sent through `client` will include the bearer token.

---

## Deployments

The `/deployments` resource lets you create and list deployments.

### List deployments

**OpenAPI**: `GET /deployments`

Query parameters:

- `limit` (number, default 20, min 1, max 100)
- `offset` (number, default 0, min 0)

```ts
// Simple list
const deployments = await client.deployments.get();

// With pagination
const deploymentsPage = await client.deployments.get({
  queryParameters: {
    limit: 50,
    offset: 0,
  },
});

// The response shape matches the OpenAPI definition:
// { deployments: Deployment[]; total: number }
```

### Create deployment

**OpenAPI**: `POST /deployments`

```ts
const body = {
  name: "my-app",
  user_id: "user-123",
  source: "remote", // or "image"
  runtime: {
    type: "nodejs",
    version: "18.0.0",
  },
  remote: {
    url: "https://github.com/user/repo.git",
    branch: "main",
  },
};

const created = await client.deployments.post({
  body,
});
```

The full shape is described in [DeployRequest](/reference#deployrequest-post-deployments)
and [DeployResponse](/reference#deployresponse).

---

## Services

The `/services` resource exposes running or configured services.

### List services

**OpenAPI**: `GET /services`

Query parameters:

- `limit` (number, default 20)
- `offset` (number, default 0)

```ts
const services = await client.services.get();

const pagedServices = await client.services.get({
  queryParameters: {
    limit: 20,
    offset: 0,
  },
});
```

The response contains `services` and `total` fields according to the schema.

### Get a service

**OpenAPI**: `GET /services/{serviceId}`

```ts
const serviceId = "01HN2K3M4N5P6Q7R8S9T0U1V2W";

const service = await client.services.byServiceId(serviceId).get();
```

### Update a service

**OpenAPI**: `PUT /services/{serviceId}`

Body schema: `ServiceUpdate`.

```ts
const updateBody = {
  name: "my-service-updated",
  description: "Updated description",
  runtime_version: "20.0.0",
  run_cmd: "npm start",
  build_cmd: "npm run build",
  port: 4000,
};

const updated = await client.services
  .byServiceId(serviceId)
  .put({ body: updateBody });
```

### Partial update

**OpenAPI**: `PATCH /services/{serviceId}`

```ts
const partialBody = {
  description: "New description only",
};

const patched = await client.services
  .byServiceId(serviceId)
  .patch({ body: partialBody });
```

### Delete a service

**OpenAPI**: `DELETE /services/{serviceId}`

```ts
await client.services.byServiceId(serviceId).delete();
```

---

## Logs

The `/logs/stream` endpoint streams logs using server‑sent events (SSE).

**OpenAPI**: `GET /logs/stream`

Required query parameters:

- `token` (string): bearer token for authentication
- `id` (string): service or deployment id

The raw API returns a `text/event-stream` stream. The exact SDK surface for
SSE depends on the generated client version. At minimum you can:

- Build a request with the required query parameters
- Send it using the underlying request adapter if you need low‑level access

```ts
const requestBuilder = client.logs.stream;

const requestInfo = requestBuilder.toGetRequestInformation({
  queryParameters: {
    token: tokenManager.accessToken,
    id: "01HN2K3M4N5P6Q7R8S9T0U1V2W",
  },
});

const response = await client.requestAdapter!.sendPrimitiveAsync<Response | undefined>(
  requestInfo,
  "Response"
);

// response is the raw HTTP response; consume the SSE stream from response.body
```

---

## Proxy

### Get proxy status

**OpenAPI**: `GET /proxy/status`

```ts
const proxyStatus = await client.proxy.status.get();
```

The response matches `ProxyStatus` (`status` field, usually `"running"`).

### Restart proxy

**OpenAPI**: `POST /proxy/restart`

```ts
const restartResult = await client.proxy.restart.post();
```

### Add proxy route

**OpenAPI**: `POST /proxy/add`

Body schema: `ProxyRoute`.

```ts
const routeBody = {
  domain: "example.com",
  upstream: "http://localhost:3000",
};

const addResult = await client.proxy.add.post({
  body: routeBody,
});
```

### Remove proxy route

**OpenAPI**: `DELETE /proxy/remove`

```ts
const removeResult = await client.proxy.remove.delete();
```

---

## System

System endpoints expose health information and management operations.

### System status

**OpenAPI**: `GET /system/status`

```ts
const systemStatus = await client.system.status.get();
```

### System info

**OpenAPI**: `GET /system/info`

```ts
const systemInfo = await client.system.info.get();
```

### Run system doctor

**OpenAPI**: `POST /system/doctor`

```ts
const doctorResult = await client.system.doctor.post();
```

### Install or upgrade dployr

**OpenAPI**: `POST /system/install`

```ts
const installBody = {
  version: "v0.1.1-beta.17", // optional, omit for latest
};

const installResult = await client.system.install.post({
  body: installBody,
});
```

### Register instance with base

**OpenAPI**: `POST /system/register`

This endpoint is typically called by base during installation or onboarding. It does **not** require authentication but validates the provided claim token against the token stored locally on the instance.

```ts
const registerBody = {
  claim: "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  instance_id: "inst_01HXYZABCDEF123456",
  // Optional overrides for token validation:
  // issuer: "https://base.dployr.dev",
  // audience: "dployr-instance",
};

const registerResult = await client.system.register.post({
  body: registerBody,
});
```
