from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cluster_savings import ClusterSavings
    from .node_savings import NodeSavings
    from .savings_day import SavingsDay

@dataclass
class OperationsSavings(AdditionalDataHolder, Parsable):
    """
    All-time time saved and time spent, per node and per cluster.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Most time saved first.
    clusters: Optional[list[ClusterSavings]] = None
    # Days with any checkpoint or restore, oldest first.
    days: Optional[list[SavingsDay]] = None
    # The generated_at_ms property
    generated_at_ms: Optional[int] = None
    # Most time saved first, at most `SAVINGS_NODE_LIMIT`; clusters are computed from every node.
    nodes: Optional[list[NodeSavings]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OperationsSavings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OperationsSavings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OperationsSavings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cluster_savings import ClusterSavings
        from .node_savings import NodeSavings
        from .savings_day import SavingsDay

        from .cluster_savings import ClusterSavings
        from .node_savings import NodeSavings
        from .savings_day import SavingsDay

        fields: dict[str, Callable[[Any], None]] = {
            "clusters": lambda n : setattr(self, 'clusters', n.get_collection_of_object_values(ClusterSavings)),
            "days": lambda n : setattr(self, 'days', n.get_collection_of_object_values(SavingsDay)),
            "generated_at_ms": lambda n : setattr(self, 'generated_at_ms', n.get_int_value()),
            "nodes": lambda n : setattr(self, 'nodes', n.get_collection_of_object_values(NodeSavings)),
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
        writer.write_collection_of_object_values("clusters", self.clusters)
        writer.write_collection_of_object_values("days", self.days)
        writer.write_int_value("generated_at_ms", self.generated_at_ms)
        writer.write_collection_of_object_values("nodes", self.nodes)
        writer.write_additional_data_value(self.additional_data)
    

