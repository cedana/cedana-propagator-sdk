from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class NodeSummary(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Bytes written by successful checkpoints on this node.
    bytes_total: Optional[int] = None
    # The checkpoints property
    checkpoints: Optional[int] = None
    # The cluster_id property
    cluster_id: Optional[str] = None
    # Source pod's PodScheduled→Ready, i.e. what the workload took to start without a checkpoint.
    cold_start_p50_ns: Optional[float] = None
    # The failed property
    failed: Optional[int] = None
    # The fallbacks property
    fallbacks: Optional[int] = None
    # The last_ms property
    last_ms: Optional[int] = None
    # The node_name property
    node_name: Optional[str] = None
    # The restore_p50_ns property
    restore_p50_ns: Optional[float] = None
    # The restores property
    restores: Optional[int] = None
    # The saved_ns property
    saved_ns: Optional[int] = None
    # Successful restores on this node with PodScheduled→Ready for both the restored pod and itscheckpoint's source pod; the three fields below are over these pairs (0 when there are none).
    savings_pairs: Optional[int] = None
    # The succeeded property
    succeeded: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NodeSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NodeSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NodeSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "bytes_total": lambda n : setattr(self, 'bytes_total', n.get_int_value()),
            "checkpoints": lambda n : setattr(self, 'checkpoints', n.get_int_value()),
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_str_value()),
            "cold_start_p50_ns": lambda n : setattr(self, 'cold_start_p50_ns', n.get_float_value()),
            "failed": lambda n : setattr(self, 'failed', n.get_int_value()),
            "fallbacks": lambda n : setattr(self, 'fallbacks', n.get_int_value()),
            "last_ms": lambda n : setattr(self, 'last_ms', n.get_int_value()),
            "node_name": lambda n : setattr(self, 'node_name', n.get_str_value()),
            "restore_p50_ns": lambda n : setattr(self, 'restore_p50_ns', n.get_float_value()),
            "restores": lambda n : setattr(self, 'restores', n.get_int_value()),
            "saved_ns": lambda n : setattr(self, 'saved_ns', n.get_int_value()),
            "savings_pairs": lambda n : setattr(self, 'savings_pairs', n.get_int_value()),
            "succeeded": lambda n : setattr(self, 'succeeded', n.get_int_value()),
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
        writer.write_int_value("bytes_total", self.bytes_total)
        writer.write_int_value("checkpoints", self.checkpoints)
        writer.write_str_value("cluster_id", self.cluster_id)
        writer.write_float_value("cold_start_p50_ns", self.cold_start_p50_ns)
        writer.write_int_value("failed", self.failed)
        writer.write_int_value("fallbacks", self.fallbacks)
        writer.write_int_value("last_ms", self.last_ms)
        writer.write_str_value("node_name", self.node_name)
        writer.write_float_value("restore_p50_ns", self.restore_p50_ns)
        writer.write_int_value("restores", self.restores)
        writer.write_int_value("saved_ns", self.saved_ns)
        writer.write_int_value("savings_pairs", self.savings_pairs)
        writer.write_int_value("succeeded", self.succeeded)
        writer.write_additional_data_value(self.additional_data)
    

