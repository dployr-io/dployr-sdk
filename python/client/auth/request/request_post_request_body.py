from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class RequestPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # User email address
    email: Optional[str] = None
    # Refresh token lifespan (e.g., "24h", "7d", "never")
    lifespan: Optional[str] = None
    # Owner secret key (required only for first owner creation)
    secret: Optional[str] = None
    # System username for role determination via groups
    username: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RequestPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RequestPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RequestPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "lifespan": lambda n : setattr(self, 'lifespan', n.get_str_value()),
            "secret": lambda n : setattr(self, 'secret', n.get_str_value()),
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
        writer.write_str_value("lifespan", self.lifespan)
        writer.write_str_value("secret", self.secret)
        writer.write_str_value("username", self.username)
        writer.write_additional_data_value(self.additional_data)
    

