from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .system_status_proxy import SystemStatus_proxy
    from .system_status_services import SystemStatus_services
    from .system_status_status import SystemStatus_status

@dataclass
class SystemStatus(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The proxy property
    proxy: Optional[SystemStatus_proxy] = None
    # The services property
    services: Optional[SystemStatus_services] = None
    # The status property
    status: Optional[SystemStatus_status] = None
    # System uptime duration
    uptime: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SystemStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SystemStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SystemStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .system_status_proxy import SystemStatus_proxy
        from .system_status_services import SystemStatus_services
        from .system_status_status import SystemStatus_status

        from .system_status_proxy import SystemStatus_proxy
        from .system_status_services import SystemStatus_services
        from .system_status_status import SystemStatus_status

        fields: dict[str, Callable[[Any], None]] = {
            "proxy": lambda n : setattr(self, 'proxy', n.get_object_value(SystemStatus_proxy)),
            "services": lambda n : setattr(self, 'services', n.get_object_value(SystemStatus_services)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SystemStatus_status)),
            "uptime": lambda n : setattr(self, 'uptime', n.get_str_value()),
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
        writer.write_object_value("proxy", self.proxy)
        writer.write_object_value("services", self.services)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("uptime", self.uptime)
        writer.write_additional_data_value(self.additional_data)
    

