from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .active_node import ActiveNode

@dataclass
class ActiveNodesResponse(AdditionalDataHolder, Parsable):
    """
    Live nodes in scope, and the ones running at least one Cedana-managed pod
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Nodes with a running Cedana-managed pod, most managed pods first
    nodes: Optional[list[ActiveNode]] = None
    # Live nodes in scope with NVIDIA GPUs
    total_gpu_nodes: Optional[int] = None
    # Physical GPUs across the live nodes in scope
    total_gpus: Optional[int] = None
    # Live nodes in scope, managed pods or not
    total_nodes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ActiveNodesResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ActiveNodesResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ActiveNodesResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .active_node import ActiveNode

        from .active_node import ActiveNode

        fields: dict[str, Callable[[Any], None]] = {
            "nodes": lambda n : setattr(self, 'nodes', n.get_collection_of_object_values(ActiveNode)),
            "total_gpu_nodes": lambda n : setattr(self, 'total_gpu_nodes', n.get_int_value()),
            "total_gpus": lambda n : setattr(self, 'total_gpus', n.get_int_value()),
            "total_nodes": lambda n : setattr(self, 'total_nodes', n.get_int_value()),
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
        writer.write_collection_of_object_values("nodes", self.nodes)
        writer.write_int_value("total_gpu_nodes", self.total_gpu_nodes)
        writer.write_int_value("total_gpus", self.total_gpus)
        writer.write_int_value("total_nodes", self.total_nodes)
        writer.write_additional_data_value(self.additional_data)
    

