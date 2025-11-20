from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .system_info_storage_devices import SystemInfo_storage_devices
    from .system_info_storage_partitions import SystemInfo_storage_partitions

@dataclass
class SystemInfo_storage(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The devices property
    devices: Optional[list[SystemInfo_storage_devices]] = None
    # The partitions property
    partitions: Optional[list[SystemInfo_storage_partitions]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SystemInfo_storage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SystemInfo_storage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SystemInfo_storage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .system_info_storage_devices import SystemInfo_storage_devices
        from .system_info_storage_partitions import SystemInfo_storage_partitions

        from .system_info_storage_devices import SystemInfo_storage_devices
        from .system_info_storage_partitions import SystemInfo_storage_partitions

        fields: dict[str, Callable[[Any], None]] = {
            "devices": lambda n : setattr(self, 'devices', n.get_collection_of_object_values(SystemInfo_storage_devices)),
            "partitions": lambda n : setattr(self, 'partitions', n.get_collection_of_object_values(SystemInfo_storage_partitions)),
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
        writer.write_collection_of_object_values("devices", self.devices)
        writer.write_collection_of_object_values("partitions", self.partitions)
        writer.write_additional_data_value(self.additional_data)
    

