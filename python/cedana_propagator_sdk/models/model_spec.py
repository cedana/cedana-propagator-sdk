from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .engine import Engine
    from .model_spec_env import ModelSpec_env
    from .model_spec_node_selector import ModelSpec_node_selector
    from .model_spec_resources import ModelSpec_resources
    from .model_spec_tolerations import ModelSpec_tolerations

@dataclass
class ModelSpec(AdditionalDataHolder, Parsable):
    """
    What a user asks for: a model on some GPUs. Everything Dynamo-shaped is derived.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The engine property
    engine: Optional[Engine] = None
    # Extra engine flags, appended after the generated ones.
    engine_args: Optional[list[str]] = None
    # The env property
    env: Optional[ModelSpec_env] = None
    # The gpus property
    gpus: Optional[int] = None
    # Secret with key `token`, for gated repos.
    hf_token_secret: Optional[str] = None
    # The image property
    image: Optional[str] = None
    # The node_selector property
    node_selector: Optional[ModelSpec_node_selector] = None
    # Serve disaggregated: a prefill and a decode worker per replica, KV moved over NIXL.Not checkpointed or parked: freezing one side of a pair breaks it.
    pd: Optional[bool] = None
    # Hugging Face repo, e.g. `Qwen/Qwen3-8B`.
    repo: Optional[str] = None
    # Worker container resources other than GPUs; no CPU or memory limits unless set here.
    resources: Optional[ModelSpec_resources] = None
    # A 40-character commit: `main` moves, and a checkpoint of other weights must not restore.
    revision: Optional[str] = None
    # The tolerations property
    tolerations: Optional[list[ModelSpec_tolerations]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ModelSpec:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ModelSpec
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ModelSpec()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .engine import Engine
        from .model_spec_env import ModelSpec_env
        from .model_spec_node_selector import ModelSpec_node_selector
        from .model_spec_resources import ModelSpec_resources
        from .model_spec_tolerations import ModelSpec_tolerations

        from .engine import Engine
        from .model_spec_env import ModelSpec_env
        from .model_spec_node_selector import ModelSpec_node_selector
        from .model_spec_resources import ModelSpec_resources
        from .model_spec_tolerations import ModelSpec_tolerations

        fields: dict[str, Callable[[Any], None]] = {
            "engine": lambda n : setattr(self, 'engine', n.get_enum_value(Engine)),
            "engine_args": lambda n : setattr(self, 'engine_args', n.get_collection_of_primitive_values(str)),
            "env": lambda n : setattr(self, 'env', n.get_object_value(ModelSpec_env)),
            "gpus": lambda n : setattr(self, 'gpus', n.get_int_value()),
            "hf_token_secret": lambda n : setattr(self, 'hf_token_secret', n.get_str_value()),
            "image": lambda n : setattr(self, 'image', n.get_str_value()),
            "node_selector": lambda n : setattr(self, 'node_selector', n.get_object_value(ModelSpec_node_selector)),
            "pd": lambda n : setattr(self, 'pd', n.get_bool_value()),
            "repo": lambda n : setattr(self, 'repo', n.get_str_value()),
            "resources": lambda n : setattr(self, 'resources', n.get_object_value(ModelSpec_resources)),
            "revision": lambda n : setattr(self, 'revision', n.get_str_value()),
            "tolerations": lambda n : setattr(self, 'tolerations', n.get_collection_of_object_values(ModelSpec_tolerations)),
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
        writer.write_enum_value("engine", self.engine)
        writer.write_collection_of_primitive_values("engine_args", self.engine_args)
        writer.write_object_value("env", self.env)
        writer.write_int_value("gpus", self.gpus)
        writer.write_str_value("hf_token_secret", self.hf_token_secret)
        writer.write_str_value("image", self.image)
        writer.write_object_value("node_selector", self.node_selector)
        writer.write_bool_value("pd", self.pd)
        writer.write_str_value("repo", self.repo)
        writer.write_object_value("resources", self.resources)
        writer.write_str_value("revision", self.revision)
        writer.write_collection_of_object_values("tolerations", self.tolerations)
        writer.write_additional_data_value(self.additional_data)
    

