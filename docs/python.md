---
outline: deep
---

# Python SDK

## Installation

```bash
pip install dployr-sdk
```

## Creating a client

```python
from dployr_sdk import create_dployr_client

# Point this at your instance address
client, token_manager = create_dployr_client("https://your-instance.example.com")
```

The factory returns:

- `client`: generated `DployrClient` bound to your base URL
- `token_manager`: helper object for storing JWTs

For the JSON shapes used in request bodies and responses, see
the [request and response shapes](/reference) page.

## Authentication

Dployr instances expect a bearer token in the `Authorization` header.

```python
# After obtaining tokens from base
access_token = "ACCESS_TOKEN_FROM_BASE"
refresh_token = "REFRESH_TOKEN_FROM_BASE"

# Store tokens on the manager
from dployr_sdk.client_factory import TokenManager

# token_manager is created by create_dployr_client
# you usually do not need to instantiate TokenManager yourself

token_manager.set_tokens(access_token, refresh_token)
```

All subsequent requests sent through `client` will include the bearer token.

---

## Deployments

The `/deployments` resource lets you create and list deployments.

### List deployments

**OpenAPI**: `GET /deployments`

Query parameters:

- `limit` (int, default 20, min 1, max 100)
- `offset` (int, default 0, min 0)

```python
# Simple list
deployments_response = await client.deployments.get()

# With pagination
deployments_response = await client.deployments.get(
    query_parameters={
        "limit": 50,
        "offset": 0,
    }
)

# The exact response shape depends on the generated models, but it matches
# the OpenAPI definition: { "deployments": [...], "total": int }
```

### Create deployment

**OpenAPI**: `POST /deployments`

```python
body = {
    "name": "my-app",
    "user_id": "user-123",
    "source": "remote",  # or "image"
    "runtime": {
        "type": "nodejs",
        "version": "18.0.0",
    },
    "remote": {
        "url": "https://github.com/user/repo.git",
        "branch": "main",
    },
}

create_response = await client.deployments.post(body)
```

The full shape is described in [DeployRequest](/reference#deployrequest-post-deployments)
and [DeployResponse](/reference#deployresponse).

---

## Services

The `/services` resource exposes running or configured services.

### List services

**OpenAPI**: `GET /services`

Query parameters:

- `limit` (int, default 20)
- `offset` (int, default 0)

```python
services_response = await client.services.get()

services_response = await client.services.get(
    query_parameters={
        "limit": 20,
        "offset": 0,
    }
)
```

The response contains `services` and `total` fields according to the schema.

### Get a service

**OpenAPI**: `GET /services/{serviceId}`

```python
service_id = "01HN2K3M4N5P6Q7R8S9T0U1V2W"
service = await client.services.by_service_id(service_id).get()
```

### Update a service

**OpenAPI**: `PUT /services/{serviceId}`

Body schema: `ServiceUpdate`.

```python
service_id = "01HN2K3M4N5P6Q7R8S9T0U1V2W"

update_body = {
    "name": "my-service-updated",
    "description": "Updated description",
    "runtime_version": "20.0.0",
    "run_cmd": "npm start",
    "build_cmd": "npm run build",
    "port": 4000,
}

updated = await client.services.by_service_id(service_id).put(update_body)
```

### Partial update

**OpenAPI**: `PATCH /services/{serviceId}`

```python
partial_body = {
    "description": "New description only",
}

patched = await client.services.by_service_id(service_id).patch(partial_body)
```

### Delete a service

**OpenAPI**: `DELETE /services/{serviceId}`

```python
await client.services.by_service_id(service_id).delete()
```

---

## Logs

The `/logs/stream` endpoint streams logs using server‑sent events (SSE).

**OpenAPI**: `GET /logs/stream`

Required query parameters:

- `token` (string): bearer token for authentication
- `id` (string): service or deployment id

The raw API returns an `text/event-stream` stream. The exact SDK surface for
SSE may depend on the generated client version. At minimum you can:

- Build a request with the required query parameters
- Send it using the underlying request adapter if you need low‑level access

```python
request_builder = client.logs.stream

request_info = request_builder.to_get_request_information(
    query_parameters={
        "token": token_manager.access_token,
        "id": "01HN2K3M4N5P6Q7R8S9T0U1V2W",
    }
)

response = await client.request_adapter.send_async(request_info, None)

# response is a raw HTTP response; consume the SSE stream from response.content
```

---

## Proxy

### Get proxy status

**OpenAPI**: `GET /proxy/status`

```python
status = await client.proxy.status.get()
```

The response matches `ProxyStatus` (`status` field, usually `"running"`).

### Restart proxy

**OpenAPI**: `POST /proxy/restart`

```python
restart_response = await client.proxy.restart.post()
```

### Add proxy route

**OpenAPI**: `POST /proxy/add`

Body schema: `ProxyRoute`.

```python
route_body = {
    "domain": "example.com",
    "upstream": "http://localhost:3000",
}

add_response = await client.proxy.add.post(route_body)
```

### Remove proxy route

**OpenAPI**: `DELETE /proxy/remove`

```python
remove_response = await client.proxy.remove.delete()
```

---

## System

System endpoints expose health information and management operations.

### System status

**OpenAPI**: `GET /system/status`

```python
system_status = await client.system.status.get()
```

### System info

**OpenAPI**: `GET /system/info`

```python
system_info = await client.system.info.get()
```

### Run system doctor

**OpenAPI**: `POST /system/doctor`

```python
doctor_result = await client.system.doctor.post()
```

### Install or upgrade dployr

**OpenAPI**: `POST /system/install`

```python
install_body = {
    "version": "v0.1.1-beta.17",  # optional, omit for latest
}

install_result = await client.system.install.post(install_body)
```
