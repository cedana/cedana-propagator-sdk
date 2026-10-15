from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ClusterSavings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The cluster_id property
    cluster_id: Optional[str] = None
    # The elapsed_ns property
    elapsed_ns: Optional[int] = None
    # The first_ms property
    first_ms: Optional[int] = None
    # Nodes with a `measured_since_ms`; only these count toward the per-node averages.
    measured_nodes: Optional[int] = None
    # The nodes property
    nodes: Optional[int] = None
    # The saved_ns property
    saved_ns: Optional[int] = None
    # Mean of the measured nodes' `saved_per_day_ns`.
    saved_per_day_per_node_ns: Optional[float] = None
    # Mean of the measured nodes' `saved_per_month_ns`.
    saved_per_month_per_node_ns: Optional[float] = None
    # The savings_pairs property
    savings_pairs: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ClusterSavings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ClusterSavings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ClusterSavings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_str_value()),
            "elapsed_ns": lambda n : setattr(self, 'elapsed_ns', n.get_int_value()),
            "first_ms": lambda n : setattr(self, 'first_ms', n.get_int_value()),
            "measured_nodes": lambda n : setattr(self, 'measured_nodes', n.get_int_value()),
            "nodes": lambda n : setattr(self, 'nodes', n.get_int_value()),
            "saved_ns": lambda n : setattr(self, 'saved_ns', n.get_int_value()),
            "saved_per_day_per_node_ns": lambda n : setattr(self, 'saved_per_day_per_node_ns', n.get_float_value()),
            "saved_per_month_per_node_ns": lambda n : setattr(self, 'saved_per_month_per_node_ns', n.get_float_value()),
            "savings_pairs": lambda n : setattr(self, 'savings_pairs', n.get_int_value()),
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
        writer.write_str_value("cluster_id", self.cluster_id)
        writer.write_int_value("elapsed_ns", self.elapsed_ns)
        writer.write_int_value("first_ms", self.first_ms)
        writer.write_int_value("measured_nodes", self.measured_nodes)
        writer.write_int_value("nodes", self.nodes)
        writer.write_int_value("saved_ns", self.saved_ns)
        writer.write_float_value("saved_per_day_per_node_ns", self.saved_per_day_per_node_ns)
        writer.write_float_value("saved_per_month_per_node_ns", self.saved_per_month_per_node_ns)
        writer.write_int_value("savings_pairs", self.savings_pairs)
        writer.write_additional_data_value(self.additional_data)
    

