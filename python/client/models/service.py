from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .blueprint import Blueprint
    from .runtime import Runtime
    from .service_env_vars import Service_env_vars

@dataclass
class Service(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The blueprint property
    blueprint: Optional[Blueprint] = None
    # The branch property
    branch: Optional[str] = None
    # The build_cmd property
    build_cmd: Optional[str] = None
    # The commit_hash property
    commit_hash: Optional[str] = None
    # The created_at property
    created_at: Optional[datetime.datetime] = None
    # The description property
    description: Optional[str] = None
    # The env_vars property
    env_vars: Optional[Service_env_vars] = None
    # The id property
    id: Optional[str] = None
    # The image property
    image: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The port property
    port: Optional[int] = None
    # The remote property
    remote: Optional[str] = None
    # The run_cmd property
    run_cmd: Optional[str] = None
    # The runtime property
    runtime: Optional[Runtime] = None
    # The runtime_version property
    runtime_version: Optional[str] = None
    # The source property
    source: Optional[str] = None
    # The static_dir property
    static_dir: Optional[str] = None
    # The status property
    status: Optional[str] = None
    # The updated_at property
    updated_at: Optional[datetime.datetime] = None
    # The working_dir property
    working_dir: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Service:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Service
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Service()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .blueprint import Blueprint
        from .runtime import Runtime
        from .service_env_vars import Service_env_vars

        from .blueprint import Blueprint
        from .runtime import Runtime
        from .service_env_vars import Service_env_vars

        fields: dict[str, Callable[[Any], None]] = {
            "blueprint": lambda n : setattr(self, 'blueprint', n.get_object_value(Blueprint)),
            "branch": lambda n : setattr(self, 'branch', n.get_str_value()),
            "build_cmd": lambda n : setattr(self, 'build_cmd', n.get_str_value()),
            "commit_hash": lambda n : setattr(self, 'commit_hash', n.get_str_value()),
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "env_vars": lambda n : setattr(self, 'env_vars', n.get_object_value(Service_env_vars)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "image": lambda n : setattr(self, 'image', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
            "remote": lambda n : setattr(self, 'remote', n.get_str_value()),
            "run_cmd": lambda n : setattr(self, 'run_cmd', n.get_str_value()),
            "runtime": lambda n : setattr(self, 'runtime', n.get_enum_value(Runtime)),
            "runtime_version": lambda n : setattr(self, 'runtime_version', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
            "static_dir": lambda n : setattr(self, 'static_dir', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "updated_at": lambda n : setattr(self, 'updated_at', n.get_datetime_value()),
            "working_dir": lambda n : setattr(self, 'working_dir', n.get_str_value()),
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
        writer.write_object_value("blueprint", self.blueprint)
        writer.write_str_value("branch", self.branch)
        writer.write_str_value("build_cmd", self.build_cmd)
        writer.write_str_value("commit_hash", self.commit_hash)
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_str_value("description", self.description)
        writer.write_object_value("env_vars", self.env_vars)
        writer.write_str_value("id", self.id)
        writer.write_str_value("image", self.image)
        writer.write_str_value("name", self.name)
        writer.write_int_value("port", self.port)
        writer.write_str_value("remote", self.remote)
        writer.write_str_value("run_cmd", self.run_cmd)
        writer.write_enum_value("runtime", self.runtime)
        writer.write_str_value("runtime_version", self.runtime_version)
        writer.write_str_value("source", self.source)
        writer.write_str_value("static_dir", self.static_dir)
        writer.write_str_value("status", self.status)
        writer.write_datetime_value("updated_at", self.updated_at)
        writer.write_str_value("working_dir", self.working_dir)
        writer.write_additional_data_value(self.additional_data)
    

