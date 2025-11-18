from enum import Enum

class TokenClaims_token_type(str, Enum):
    Access = "access",
    Refresh = "refresh",

