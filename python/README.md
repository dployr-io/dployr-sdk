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
client, token_manager = create_dployr_client('https://your-dployr-instance.com')

# Login to get authentication tokens
auth = await client.auth.request.post({
    'email': 'user@example.com'
})

# Store tokens for authenticated requests
token_manager.set_tokens(auth.access_token, auth.refresh_token)

# Now you can make authenticated API calls
deployments = await client.deployments.get()
services = await client.services.get()
```

## Authentication

The SDK uses JWT-based authentication with access and refresh tokens:

- **Access tokens** are short-lived (~10 minutes) and used for API requests
- **Refresh tokens** are long-lived (24+ hours) and used to obtain new access tokens

Use the `TokenManager` to store and manage your tokens after login.

## Documentation

For full API reference and guides, visit [dployr docs](https://docs.dployr.dev).
