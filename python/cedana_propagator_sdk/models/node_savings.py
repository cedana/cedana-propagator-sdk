from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class NodeSavings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The checkpoints property
    checkpoints: Optional[int] = None
    # The cluster_id property
    cluster_id: Optional[str] = None
    # Time Cedana spent checkpointing and restoring on this node, all attempts.
    elapsed_ns: Optional[int] = None
    # First checkpoint or restore started on this node.
    first_ms: Optional[int] = None
    # The last_ms property
    last_ms: Optional[int] = None
    # First operation here with pod start times recorded; the averages run from here to now, and are 0 without one.
    measured_since_ms: Optional[int] = None
    # The node_name property
    node_name: Optional[str] = None
    # The restores property
    restores: Optional[int] = None
    # Sum over those pairs of source cold start minus restore, floored at 0 per pair.
    saved_ns: Optional[int] = None
    # `saved_ns` per 24h since `measured_since_ms` (at least one day).
    saved_per_day_ns: Optional[float] = None
    # `saved_ns` per calendar month since `measured_since_ms`, counting the first and current months.
    saved_per_month_ns: Optional[float] = None
    # Restores here with PodScheduled→Ready for both the restored pod and its checkpoint's source pod.
    savings_pairs: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NodeSavings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NodeSavings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NodeSavings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "checkpoints": lambda n : setattr(self, 'checkpoints', n.get_int_value()),
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_str_value()),
            "elapsed_ns": lambda n : setattr(self, 'elapsed_ns', n.get_int_value()),
            "first_ms": lambda n : setattr(self, 'first_ms', n.get_int_value()),
            "last_ms": lambda n : setattr(self, 'last_ms', n.get_int_value()),
            "measured_since_ms": lambda n : setattr(self, 'measured_since_ms', n.get_int_value()),
            "node_name": lambda n : setattr(self, 'node_name', n.get_str_value()),
            "restores": lambda n : setattr(self, 'restores', n.get_int_value()),
            "saved_ns": lambda n : setattr(self, 'saved_ns', n.get_int_value()),
            "saved_per_day_ns": lambda n : setattr(self, 'saved_per_day_ns', n.get_float_value()),
            "saved_per_month_ns": lambda n : setattr(self, 'saved_per_month_ns', n.get_float_value()),
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
        writer.write_int_value("checkpoints", self.checkpoints)
        writer.write_str_value("cluster_id", self.cluster_id)
        writer.write_int_value("elapsed_ns", self.elapsed_ns)
        writer.write_int_value("first_ms", self.first_ms)
        writer.write_int_value("last_ms", self.last_ms)
        writer.write_int_value("measured_since_ms", self.measured_since_ms)
        writer.write_str_value("node_name", self.node_name)
        writer.write_int_value("restores", self.restores)
        writer.write_int_value("saved_ns", self.saved_ns)
        writer.write_float_value("saved_per_day_ns", self.saved_per_day_ns)
        writer.write_float_value("saved_per_month_ns", self.saved_per_month_ns)
        writer.write_int_value("savings_pairs", self.savings_pairs)
        writer.write_additional_data_value(self.additional_data)
    

