/**
 * MIT License
 * Copyright (c) 2025 Emmanuel Madehin
 * See LICENSE file for full license text
 */

import { FetchRequestAdapter } from "@microsoft/kiota-http-fetchlibrary";
import {
  AuthenticationProvider,
  RequestAdapter,
  RequestInformation,
} from "@microsoft/kiota-abstractions";
import { createDployrClient as createKiotaClient } from "../client/dployrClient.js";

/**
 * Manages authentication tokens for API requests.
 * 
 * Stores both access tokens (short-lived, ~10 minutes) and refresh tokens 
 * (long-lived, 24+ hours) for authenticating with the Dployr API.
 */
class TokenManager {
  accessToken: string | null = null;
  refreshToken: string | null = null;

  /**
   * Set the access token for API authentication.
   * @param token - JWT access token from login or refresh endpoint
   */
  setAccessToken(token: string) {
    this.accessToken = token;
  }

  /**
   * Set both access and refresh tokens at once.
   * @param access - JWT access token
   * @param refresh - Optional JWT refresh token for token renewal
   */
  setTokens(access: string, refresh?: string) {
    this.accessToken = access;
    if (refresh) this.refreshToken = refresh;
  }
}

/**
 * Authentication provider that adds Bearer token to API requests.
 * 
 * Automatically injects the access token into the Authorization header
 * of every API request when available.
 */
class DployrAuthProvider implements AuthenticationProvider {
  constructor(private tokenManager: TokenManager) { }

  public authenticateRequest = async (
    request: RequestInformation,
  ): Promise<void> => {
    if (this.tokenManager.accessToken) {
      request.headers.add("Authorization", `Bearer ${this.tokenManager.accessToken}`);
    }
  };
}

/**
 * Create a Dployr API client with authentication support.
 * 
 * Main entry point for interacting with the Dployr API. Provides access to all 
 * endpoints including authentication, deployments, services, logs, and system management.
 * 
 * @param baseUrl - The base URL of your Dployr instance (default: http://localhost:7879)
 * @returns Object containing the API client and token manager
 * 
 * @example
 * ```typescript
 * import { createDployrClient } from '@dployr-io/dployr-sdk';
 * 
 * // Create client for your Dployr instance
 * const { client, tokenManager } = createDployrClient('https://dployr.example.com');
 * 
 * // Login to get tokens
 * const auth = await client.auth.request.post({
 *   email: 'user@example.com'
 * });
 * 
 * // Store tokens for subsequent requests
 * tokenManager.setTokens(auth.access_token, auth.refresh_token);
 * 
 * // Now make authenticated requests
 * const services = await client.services.get();
 * const deployments = await client.deployments.get();
 * ```
 */
export function createDployrClient(baseUrl = "http://localhost:7879") {
  const tokenManager = new TokenManager();
  const authProvider = new DployrAuthProvider(tokenManager);

  const adapter: RequestAdapter = new FetchRequestAdapter(authProvider);
  adapter.baseUrl = baseUrl;

  const client = createKiotaClient(adapter);

  return { client, tokenManager };
}
