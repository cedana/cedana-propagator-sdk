from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .model_spec import ModelSpec

@dataclass
class CreateProfile(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The cluster_id property
    cluster_id: Optional[UUID] = None
    # The estimated_cold_start_ms property
    estimated_cold_start_ms: Optional[int] = None
    # The name callers use; defaults to the profile id.
    logical_model: Optional[str] = None
    # The max_queue_depth property
    max_queue_depth: Optional[int] = None
    # The max_replicas property
    max_replicas: Optional[int] = None
    # The min_replicas property
    min_replicas: Optional[int] = None
    # What a user asks for: a model on some GPUs. Everything Dynamo-shaped is derived.
    model: Optional[ModelSpec] = None
    # The namespace property
    namespace: Optional[str] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # The scale_down_idle_seconds property
    scale_down_idle_seconds: Optional[int] = None
    # The target_concurrency property
    target_concurrency: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .model_spec import ModelSpec

        from .model_spec import ModelSpec

        fields: dict[str, Callable[[Any], None]] = {
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_uuid_value()),
            "estimated_cold_start_ms": lambda n : setattr(self, 'estimated_cold_start_ms', n.get_int_value()),
            "logical_model": lambda n : setattr(self, 'logical_model', n.get_str_value()),
            "max_queue_depth": lambda n : setattr(self, 'max_queue_depth', n.get_int_value()),
            "max_replicas": lambda n : setattr(self, 'max_replicas', n.get_int_value()),
            "min_replicas": lambda n : setattr(self, 'min_replicas', n.get_int_value()),
            "model": lambda n : setattr(self, 'model', n.get_object_value(ModelSpec)),
            "namespace": lambda n : setattr(self, 'namespace', n.get_str_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "scale_down_idle_seconds": lambda n : setattr(self, 'scale_down_idle_seconds', n.get_int_value()),
            "target_concurrency": lambda n : setattr(self, 'target_concurrency', n.get_int_value()),
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
        writer.write_uuid_value("cluster_id", self.cluster_id)
        writer.write_int_value("estimated_cold_start_ms", self.estimated_cold_start_ms)
        writer.write_str_value("logical_model", self.logical_model)
        writer.write_int_value("max_queue_depth", self.max_queue_depth)
        writer.write_int_value("max_replicas", self.max_replicas)
        writer.write_int_value("min_replicas", self.min_replicas)
        writer.write_object_value("model", self.model)
        writer.write_str_value("namespace", self.namespace)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_int_value("scale_down_idle_seconds", self.scale_down_idle_seconds)
        writer.write_int_value("target_concurrency", self.target_concurrency)
        writer.write_additional_data_value(self.additional_data)
    

