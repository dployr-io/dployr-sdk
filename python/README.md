# dployr-sdk

Python SDK for interacting with [dployr](https://github.com/dployr-io/dployr).

## Installation

```bash
pip install dployr-sdk
# or
poetry add dployr-sdk
# or
uv add dployr-sdk
```

## Usage

```python
from dployr_sdk import create_dployr_client

# Connect to your Dployr instance
client, token_manager = create_dployr_client("https://your-dployr-instance.com")

# Obtain a JWT access token from your dployr base server
# (see https://docs.dployr.dev/auth for details on how to authenticate with base)
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."  # issued by base

# Set the token so all requests to the instance are authenticated
token_manager.set_access_token(access_token)

# Now you can make authenticated API calls to the instance
deployments_response = await client.deployments.get()
services_response = await client.services.get()

deployments = deployments_response.deployments or []
services = services_response.services or []
```

## Authentication

The SDK uses JWT-based authentication with tokens **issued by base**:

- **Access tokens** are short-lived (~10 minutes) and used for API requests to instances
- **Refresh tokens** are long-lived (24+ hours) and used to obtain new access tokens from base

Use the `TokenManager` to store and manage the tokens you receive from base. The SDK does not
auto-refresh tokens; if an access token expires you should:

1. Call your base server's refresh endpoint to get a new access token.
2. Update the SDK's token manager, e.g. `token_manager.set_access_token(new_access_token)`.
3. Retry the failed request if needed.

For the full authentication flow and examples of obtaining tokens from base, see
https://docs.dployr.dev/auth.

## Client overview

`create_dployr_client` returns a `client` with:

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

```python
deployments_response = await client.deployments.get({
    "limit": 20,
    "offset": 0,
})

deployments = deployments_response.deployments or []
```

List services:

```python
services_response = await client.services.get({
    "limit": 20,
    "offset": 0,
})

services = services_response.services or []
```

Get a single service:

```python
service = await client.services.by_service_id("service-id").get()
```

Stream logs for a service or deployment (Server-Sent Events):

```python
response = await client.logs.stream.get({
    "token": access_token,
    "id": "service-or-deployment-id",
})
# Handle the text/event-stream response using your HTTP client.
```

Check system status:

```python
status = await client.system.status.get()
```

Restart proxy:

```python
result = await client.proxy.restart.post()
```

## Documentation

For full API reference and guides for the Python SDK, visit
https://sdk.dployr.dev/python.
