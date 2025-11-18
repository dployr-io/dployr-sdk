from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.role import Role

@dataclass
class RolePutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # User role hierarchy (owner > admin > developer > viewer):- **owner**: Full system control, manage admins, uninstall dployr- **admin**: Secrets, users, proxies, shell access- **developer**: Deploy apps, view logs, events, resource graph- **viewer**: Read-only access to services
    role: Optional[Role] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RolePutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RolePutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RolePutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ....models.role import Role

        from ....models.role import Role

        fields: dict[str, Callable[[Any], None]] = {
            "role": lambda n : setattr(self, 'role', n.get_enum_value(Role)),
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
        writer.write_enum_value("role", self.role)
        writer.write_additional_data_value(self.additional_data)
    

