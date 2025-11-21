from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class RegisterInstanceRequest(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Expected token audience (for validation)
    audience: Optional[str] = None
    # Signed claim token issued by base
    claim: Optional[str] = None
    # Unique identifier assigned to this instance by base
    instance_id: Optional[str] = None
    # Expected token issuer (for validation)
    issuer: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RegisterInstanceRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RegisterInstanceRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RegisterInstanceRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "audience": lambda n : setattr(self, 'audience', n.get_str_value()),
            "claim": lambda n : setattr(self, 'claim', n.get_str_value()),
            "instance_id": lambda n : setattr(self, 'instance_id', n.get_str_value()),
            "issuer": lambda n : setattr(self, 'issuer', n.get_str_value()),
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
        writer.write_str_value("audience", self.audience)
        writer.write_str_value("claim", self.claim)
        writer.write_str_value("instance_id", self.instance_id)
        writer.write_str_value("issuer", self.issuer)
        writer.write_additional_data_value(self.additional_data)
    

