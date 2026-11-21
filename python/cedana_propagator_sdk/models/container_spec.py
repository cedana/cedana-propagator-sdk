from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .container_spec_env import ContainerSpec_env
    from .container_spec_node_selector import ContainerSpec_node_selector
    from .container_spec_resources import ContainerSpec_resources
    from .container_spec_secret_files import ContainerSpec_secret_files
    from .container_spec_tolerations import ContainerSpec_tolerations

@dataclass
class ContainerSpec(AdditionalDataHolder, Parsable):
    """
    Any HTTP server image as one GPU worker: no Dynamo frontend, no weights download.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The args property
    args: Optional[list[str]] = None
    # The image entrypoint when empty.
    command: Optional[list[str]] = None
    # The env property
    env: Optional[ContainerSpec_env] = None
    # The gpus property
    gpus: Optional[int] = None
    # Image reference with a digest (`name@sha256:...`): a tag can move under a checkpoint.
    image: Optional[str] = None
    # Registry Secrets in the profile's namespace, for an image in a private registry.Not in the checkpoint name: pull credentials do not change the process.
    image_pull_secrets: Optional[list[str]] = None
    # The live_path property
    live_path: Optional[str] = None
    # The id the server lists in `GET /v1/models`; the router sends it upstream.
    model_id: Optional[str] = None
    # The node_selector property
    node_selector: Optional[ContainerSpec_node_selector] = None
    # The port the server listens on.
    port: Optional[int] = None
    # Readiness path: the pod is ready once the model is loaded.
    ready_path: Optional[str] = None
    # The resources property
    resources: Optional[ContainerSpec_resources] = None
    # Mount directory to Secret name. Each key of the Secret is a file in the directory,read-only. A rotated Secret keeps the checkpoint: only the path and name are hashed.
    secret_files: Optional[ContainerSpec_secret_files] = None
    # The tolerations property
    tolerations: Optional[list[ContainerSpec_tolerations]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContainerSpec:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContainerSpec
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ContainerSpec()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .container_spec_env import ContainerSpec_env
        from .container_spec_node_selector import ContainerSpec_node_selector
        from .container_spec_resources import ContainerSpec_resources
        from .container_spec_secret_files import ContainerSpec_secret_files
        from .container_spec_tolerations import ContainerSpec_tolerations

        from .container_spec_env import ContainerSpec_env
        from .container_spec_node_selector import ContainerSpec_node_selector
        from .container_spec_resources import ContainerSpec_resources
        from .container_spec_secret_files import ContainerSpec_secret_files
        from .container_spec_tolerations import ContainerSpec_tolerations

        fields: dict[str, Callable[[Any], None]] = {
            "args": lambda n : setattr(self, 'args', n.get_collection_of_primitive_values(str)),
            "command": lambda n : setattr(self, 'command', n.get_collection_of_primitive_values(str)),
            "env": lambda n : setattr(self, 'env', n.get_object_value(ContainerSpec_env)),
            "gpus": lambda n : setattr(self, 'gpus', n.get_int_value()),
            "image": lambda n : setattr(self, 'image', n.get_str_value()),
            "image_pull_secrets": lambda n : setattr(self, 'image_pull_secrets', n.get_collection_of_primitive_values(str)),
            "live_path": lambda n : setattr(self, 'live_path', n.get_str_value()),
            "model_id": lambda n : setattr(self, 'model_id', n.get_str_value()),
            "node_selector": lambda n : setattr(self, 'node_selector', n.get_object_value(ContainerSpec_node_selector)),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
            "ready_path": lambda n : setattr(self, 'ready_path', n.get_str_value()),
            "resources": lambda n : setattr(self, 'resources', n.get_object_value(ContainerSpec_resources)),
            "secret_files": lambda n : setattr(self, 'secret_files', n.get_object_value(ContainerSpec_secret_files)),
            "tolerations": lambda n : setattr(self, 'tolerations', n.get_collection_of_object_values(ContainerSpec_tolerations)),
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
        writer.write_collection_of_primitive_values("args", self.args)
        writer.write_collection_of_primitive_values("command", self.command)
        writer.write_object_value("env", self.env)
        writer.write_int_value("gpus", self.gpus)
        writer.write_str_value("image", self.image)
        writer.write_collection_of_primitive_values("image_pull_secrets", self.image_pull_secrets)
        writer.write_str_value("live_path", self.live_path)
        writer.write_str_value("model_id", self.model_id)
        writer.write_object_value("node_selector", self.node_selector)
        writer.write_int_value("port", self.port)
        writer.write_str_value("ready_path", self.ready_path)
        writer.write_object_value("resources", self.resources)
        writer.write_object_value("secret_files", self.secret_files)
        writer.write_collection_of_object_values("tolerations", self.tolerations)
        writer.write_additional_data_value(self.additional_data)
    

