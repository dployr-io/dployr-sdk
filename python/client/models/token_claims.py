from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .token_claims_token_type import TokenClaims_token_type

@dataclass
class TokenClaims(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The email property
    email: Optional[str] = None
    # Expiration timestamp (Unix)
    exp: Optional[int] = None
    # Issued at timestamp (Unix)
    iat: Optional[int] = None
    # Type of JWT token
    token_type: Optional[TokenClaims_token_type] = None
    # System username
    username: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TokenClaims:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TokenClaims
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TokenClaims()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .token_claims_token_type import TokenClaims_token_type

        from .token_claims_token_type import TokenClaims_token_type

        fields: dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "exp": lambda n : setattr(self, 'exp', n.get_int_value()),
            "iat": lambda n : setattr(self, 'iat', n.get_int_value()),
            "token_type": lambda n : setattr(self, 'token_type', n.get_enum_value(TokenClaims_token_type)),
            "username": lambda n : setattr(self, 'username', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("email", self.email)
        writer.write_int_value("exp", self.exp)
        writer.write_int_value("iat", self.iat)
        writer.write_enum_value("token_type", self.token_type)
        writer.write_str_value("username", self.username)
        writer.write_additional_data_value(self.additional_data)
    

