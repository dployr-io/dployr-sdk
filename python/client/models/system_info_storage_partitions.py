from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SystemInfo_storage_partitions(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The available property
    available: Optional[str] = None
    # The filesystem property
    filesystem: Optional[str] = None
    # The mountpoint property
    mountpoint: Optional[str] = None
    # The size property
    size: Optional[str] = None
    # The use_percent property
    use_percent: Optional[str] = None
    # The used property
    used: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SystemInfo_storage_partitions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SystemInfo_storage_partitions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SystemInfo_storage_partitions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "available": lambda n : setattr(self, 'available', n.get_str_value()),
            "filesystem": lambda n : setattr(self, 'filesystem', n.get_str_value()),
            "mountpoint": lambda n : setattr(self, 'mountpoint', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_str_value()),
            "use_percent": lambda n : setattr(self, 'use_percent', n.get_str_value()),
            "used": lambda n : setattr(self, 'used', n.get_str_value()),
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
        writer.write_str_value("available", self.available)
        writer.write_str_value("filesystem", self.filesystem)
        writer.write_str_value("mountpoint", self.mountpoint)
        writer.write_str_value("size", self.size)
        writer.write_str_value("use_percent", self.use_percent)
        writer.write_str_value("used", self.used)
        writer.write_additional_data_value(self.additional_data)
    

