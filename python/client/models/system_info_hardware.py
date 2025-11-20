from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SystemInfo_hardware(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The arch property
    arch: Optional[str] = None
    # The cpu_count property
    cpu_count: Optional[int] = None
    # The hostname property
    hostname: Optional[str] = None
    # The kernel property
    kernel: Optional[str] = None
    # The mem_free property
    mem_free: Optional[str] = None
    # The mem_total property
    mem_total: Optional[str] = None
    # The mem_used property
    mem_used: Optional[str] = None
    # The os property
    os: Optional[str] = None
    # The swap_total property
    swap_total: Optional[str] = None
    # The swap_used property
    swap_used: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SystemInfo_hardware:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SystemInfo_hardware
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SystemInfo_hardware()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "arch": lambda n : setattr(self, 'arch', n.get_str_value()),
            "cpu_count": lambda n : setattr(self, 'cpu_count', n.get_int_value()),
            "hostname": lambda n : setattr(self, 'hostname', n.get_str_value()),
            "kernel": lambda n : setattr(self, 'kernel', n.get_str_value()),
            "mem_free": lambda n : setattr(self, 'mem_free', n.get_str_value()),
            "mem_total": lambda n : setattr(self, 'mem_total', n.get_str_value()),
            "mem_used": lambda n : setattr(self, 'mem_used', n.get_str_value()),
            "os": lambda n : setattr(self, 'os', n.get_str_value()),
            "swap_total": lambda n : setattr(self, 'swap_total', n.get_str_value()),
            "swap_used": lambda n : setattr(self, 'swap_used', n.get_str_value()),
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
        writer.write_str_value("arch", self.arch)
        writer.write_int_value("cpu_count", self.cpu_count)
        writer.write_str_value("hostname", self.hostname)
        writer.write_str_value("kernel", self.kernel)
        writer.write_str_value("mem_free", self.mem_free)
        writer.write_str_value("mem_total", self.mem_total)
        writer.write_str_value("mem_used", self.mem_used)
        writer.write_str_value("os", self.os)
        writer.write_str_value("swap_total", self.swap_total)
        writer.write_str_value("swap_used", self.swap_used)
        writer.write_additional_data_value(self.additional_data)
    

