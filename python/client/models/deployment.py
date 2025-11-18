from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .blueprint import Blueprint
    from .deployment_status import DeploymentStatus

@dataclass
class Deployment(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The config property
    config: Optional[Blueprint] = None
    # The created_at property
    created_at: Optional[datetime.datetime] = None
    # The id property
    id: Optional[str] = None
    # The metadata property
    metadata: Optional[str] = None
    # The status property
    status: Optional[DeploymentStatus] = None
    # The updated_at property
    updated_at: Optional[datetime.datetime] = None
    # Email of the user who created the deployment
    user_email: Optional[str] = None
    # ID of the user who created the deployment
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Deployment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Deployment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Deployment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .blueprint import Blueprint
        from .deployment_status import DeploymentStatus

        from .blueprint import Blueprint
        from .deployment_status import DeploymentStatus

        fields: dict[str, Callable[[Any], None]] = {
            "config": lambda n : setattr(self, 'config', n.get_object_value(Blueprint)),
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(DeploymentStatus)),
            "updated_at": lambda n : setattr(self, 'updated_at', n.get_datetime_value()),
            "user_email": lambda n : setattr(self, 'user_email', n.get_str_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_object_value("config", self.config)
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_str_value("id", self.id)
        writer.write_str_value("metadata", self.metadata)
        writer.write_enum_value("status", self.status)
        writer.write_datetime_value("updated_at", self.updated_at)
        writer.write_str_value("user_email", self.user_email)
        writer.write_str_value("user_id", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    

