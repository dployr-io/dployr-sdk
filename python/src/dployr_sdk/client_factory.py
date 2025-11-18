"""
MIT License
Copyright (c) 2025 Emmanuel Madehin
See LICENSE file for full license text

Factory for creating Dployr API clients with authentication.
"""

from typing import Optional, Dict, Tuple
from kiota_abstractions.authentication import AuthenticationProvider
from kiota_abstractions.request_information import RequestInformation
from kiota_http.httpx_request_adapter import HttpxRequestAdapter

try:
    from ..client.dployr_client import DployrClient
except ImportError:
    DployrClient = None


class TokenManager:
    """
    Manages authentication tokens for API requests.
    
    Stores both access tokens (short-lived, ~10 minutes) and refresh tokens 
    (long-lived, 24+ hours) for authenticating with the Dployr API.
    
    Attributes:
        access_token: JWT access token for API authentication
        refresh_token: JWT refresh token for obtaining new access tokens
    """

    def __init__(self):
        self.access_token: Optional[str] = None
        self.refresh_token: Optional[str] = None

    def set_access_token(self, token: str) -> None:
        """
        Set the access token for API authentication.
        
        Args:
            token: JWT access token from login or refresh endpoint
        """
        self.access_token = token

    def set_tokens(self, access: str, refresh: Optional[str] = None) -> None:
        """
        Set both access and refresh tokens at once.
        
        Args:
            access: JWT access token
            refresh: Optional JWT refresh token for token renewal
        """
        self.access_token = access
        if refresh:
            self.refresh_token = refresh


class DployrAuthProvider(AuthenticationProvider):
    """
    Authentication provider that adds Bearer token to API requests.
    
    Automatically injects the access token into the Authorization header
    of every API request when available.
    """

    def __init__(self, token_manager: TokenManager):
        """
        Initialize the auth provider.
        
        Args:
            token_manager: TokenManager instance containing the access token
        """
        self.token_manager = token_manager

    async def authenticate_request(
        self, 
        request: RequestInformation, 
        additional_authentication_context: Optional[Dict[str, object]] = None
    ) -> None:
        """
        Add authentication header to the request.
        
        Args:
            request: The HTTP request to authenticate
            additional_authentication_context: Optional additional context
        """
        if self.token_manager.access_token:
            if not request.headers:
                request.headers = {}
            request.headers["Authorization"] = f"Bearer {self.token_manager.access_token}"


def create_dployr_client(base_url: str = "http://localhost:7879") -> Tuple[object, TokenManager]:
    """
    Create a Dployr API client with authentication support.
    
    This is the main entry point for creating a client to interact with
    the Dployr API. The returned client provides access to all API endpoints
    including authentication, deployments, services, logs, and system management.
    
    Args:
        base_url: The base URL of your Dployr instance. 
                 Defaults to http://localhost:7879 for local development.
    
    Returns:
        A tuple containing:
        - client: The Dployr API client with all endpoint methods
        - token_manager: TokenManager for setting authentication tokens
    
    Example:
        >>> from dployr_sdk import create_dployr_client
        >>> 
        >>> # Create client for your Dployr instance
        >>> client, token_manager = create_dployr_client('https://dployr.example.com')
        >>> 
        >>> # Login to get tokens
        >>> auth_response = await client.auth.request.post({
        ...     'email': 'user@example.com'
        ... })
        >>> 
        >>> # Store tokens for subsequent requests
        >>> token_manager.set_tokens(
        ...     auth_response.access_token,
        ...     auth_response.refresh_token
        ... )
        >>> 
        >>> # Now make authenticated requests
        >>> services = await client.services.get()
        >>> deployments = await client.deployments.get()
    """
    token_manager = TokenManager()
    auth_provider = DployrAuthProvider(token_manager)

    adapter = HttpxRequestAdapter(auth_provider)
    adapter.base_url = base_url

    client = DployrClient(adapter)

    return client, token_manager
