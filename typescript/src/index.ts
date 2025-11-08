import { FetchRequestAdapter } from "@microsoft/kiota-http-fetchlibrary";
import {
  AuthenticationProvider,
  RequestAdapter,
  RequestInformation,
} from "@microsoft/kiota-abstractions";
import { createDployrClient as createKiotaClient } from "../client/dployrClient.js";

/** Simple token manager */
class TokenManager {
  accessToken: string | null = null;
  refreshToken: string | null = null;

  setAccessToken(token: string) {
    this.accessToken = token;
  }

  setTokens(access: string, refresh?: string) {
    this.accessToken = access;
    if (refresh) this.refreshToken = refresh;
  }
}

/** Kiota auth provider that injects the access token */
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
 * Factory to create a Kiota-based Dployr client with auth
 */
export function createDployrClient(baseUrl = "http://localhost:7879") {
  const tokenManager = new TokenManager();
  const authProvider = new DployrAuthProvider(tokenManager);

  const adapter: RequestAdapter = new FetchRequestAdapter(authProvider);
  adapter.baseUrl = baseUrl;

  const client = createKiotaClient(adapter);

  return { client, tokenManager };
}

