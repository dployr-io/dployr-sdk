from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .deploy_request_env_vars import DeployRequest_env_vars
    from .deploy_request_secrets import DeployRequest_secrets
    from .deploy_request_source import DeployRequest_source
    from .remote_obj import RemoteObj
    from .runtime_obj import RuntimeObj

@dataclass
class DeployRequest(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The build_cmd property
    build_cmd: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The dns_provider property
    dns_provider: Optional[str] = None
    # The domain property
    domain: Optional[str] = None
    # The env_vars property
    env_vars: Optional[DeployRequest_env_vars] = None
    # The image property
    image: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The port property
    port: Optional[int] = None
    # The remote property
    remote: Optional[RemoteObj] = None
    # The run_cmd property
    run_cmd: Optional[str] = None
    # The runtime property
    runtime: Optional[RuntimeObj] = None
    # The secrets property
    secrets: Optional[DeployRequest_secrets] = None
    # The source property
    source: Optional[DeployRequest_source] = None
    # The static_dir property
    static_dir: Optional[str] = None
    # The user_id property
    user_id: Optional[str] = None
    # The version property
    version: Optional[str] = None
    # The working_dir property
    working_dir: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeployRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeployRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeployRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .deploy_request_env_vars import DeployRequest_env_vars
        from .deploy_request_secrets import DeployRequest_secrets
        from .deploy_request_source import DeployRequest_source
        from .remote_obj import RemoteObj
        from .runtime_obj import RuntimeObj

        from .deploy_request_env_vars import DeployRequest_env_vars
        from .deploy_request_secrets import DeployRequest_secrets
        from .deploy_request_source import DeployRequest_source
        from .remote_obj import RemoteObj
        from .runtime_obj import RuntimeObj

        fields: dict[str, Callable[[Any], None]] = {
            "build_cmd": lambda n : setattr(self, 'build_cmd', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "dns_provider": lambda n : setattr(self, 'dns_provider', n.get_str_value()),
            "domain": lambda n : setattr(self, 'domain', n.get_str_value()),
            "env_vars": lambda n : setattr(self, 'env_vars', n.get_object_value(DeployRequest_env_vars)),
            "image": lambda n : setattr(self, 'image', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
            "remote": lambda n : setattr(self, 'remote', n.get_object_value(RemoteObj)),
            "run_cmd": lambda n : setattr(self, 'run_cmd', n.get_str_value()),
            "runtime": lambda n : setattr(self, 'runtime', n.get_object_value(RuntimeObj)),
            "secrets": lambda n : setattr(self, 'secrets', n.get_object_value(DeployRequest_secrets)),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(DeployRequest_source)),
            "static_dir": lambda n : setattr(self, 'static_dir', n.get_str_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_str_value("build_cmd", self.build_cmd)
        writer.write_str_value("description", self.description)
        writer.write_str_value("dns_provider", self.dns_provider)
        writer.write_str_value("domain", self.domain)
        writer.write_object_value("env_vars", self.env_vars)
        writer.write_str_value("image", self.image)
        writer.write_str_value("name", self.name)
        writer.write_int_value("port", self.port)
        writer.write_object_value("remote", self.remote)
        writer.write_str_value("run_cmd", self.run_cmd)
        writer.write_object_value("runtime", self.runtime)
        writer.write_object_value("secrets", self.secrets)
        writer.write_enum_value("source", self.source)
        writer.write_str_value("static_dir", self.static_dir)
        writer.write_str_value("user_id", self.user_id)
        writer.write_str_value("version", self.version)
        writer.write_str_value("working_dir", self.working_dir)
        writer.write_additional_data_value(self.additional_data)
    

