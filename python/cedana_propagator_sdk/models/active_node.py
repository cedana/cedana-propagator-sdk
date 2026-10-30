from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .active_pod import ActivePod

@dataclass
class ActiveNode(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The cluster_id property
    cluster_id: Optional[UUID] = None
    # The cluster_name property
    cluster_name: Optional[str] = None
    # The gpu_product property
    gpu_product: Optional[str] = None
    # Physical GPUs on the node; null for a node without NVIDIA GPUs
    gpus: Optional[int] = None
    # The id property
    id: Optional[UUID] = None
    # The name property
    name: Optional[str] = None
    # nvidia.com/gpu requested by those pods
    pod_gpus: Optional[int] = None
    # Running pods on this node with `runtimeClassName: cedana`, by name
    pods: Optional[list[ActivePod]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ActiveNode:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ActiveNode
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ActiveNode()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .active_pod import ActivePod

        from .active_pod import ActivePod

        fields: dict[str, Callable[[Any], None]] = {
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_uuid_value()),
            "cluster_name": lambda n : setattr(self, 'cluster_name', n.get_str_value()),
            "gpu_product": lambda n : setattr(self, 'gpu_product', n.get_str_value()),
            "gpus": lambda n : setattr(self, 'gpus', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "pod_gpus": lambda n : setattr(self, 'pod_gpus', n.get_int_value()),
            "pods": lambda n : setattr(self, 'pods', n.get_collection_of_object_values(ActivePod)),
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
        writer.write_str_value("cluster_name", self.cluster_name)
        writer.write_str_value("gpu_product", self.gpu_product)
        writer.write_int_value("gpus", self.gpus)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("name", self.name)
        writer.write_int_value("pod_gpus", self.pod_gpus)
        writer.write_collection_of_object_values("pods", self.pods)
        writer.write_additional_data_value(self.additional_data)
    

