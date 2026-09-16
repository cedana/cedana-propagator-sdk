from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class OrgCheckpointSavings(AdditionalDataHolder, Parsable):
    """
    Organization-level checkpoint savings summary
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The avg_checkpoint_interval_seconds property
    avg_checkpoint_interval_seconds: Optional[float] = None
    # The pods_protected property
    pods_protected: Optional[int] = None
    # The refreshed_at property
    refreshed_at: Optional[datetime.datetime] = None
    # The total_checkpoint_overhead_ns property
    total_checkpoint_overhead_ns: Optional[int] = None
    # The total_checkpoint_storage_bytes property
    total_checkpoint_storage_bytes: Optional[int] = None
    # The total_checkpoints property
    total_checkpoints: Optional[int] = None
    # Total estimated savings across all pods (spot vs on-demand)
    total_estimated_savings: Optional[float] = None
    # The total_heartbeat_checkpoints property
    total_heartbeat_checkpoints: Optional[int] = None
    # The total_manual_checkpoints property
    total_manual_checkpoints: Optional[int] = None
    # The total_time_protected_seconds property
    total_time_protected_seconds: Optional[float] = None
    # The worst_case_recovery_point_seconds property
    worst_case_recovery_point_seconds: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrgCheckpointSavings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrgCheckpointSavings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrgCheckpointSavings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "avg_checkpoint_interval_seconds": lambda n : setattr(self, 'avg_checkpoint_interval_seconds', n.get_float_value()),
            "pods_protected": lambda n : setattr(self, 'pods_protected', n.get_int_value()),
            "refreshed_at": lambda n : setattr(self, 'refreshed_at', n.get_datetime_value()),
            "total_checkpoint_overhead_ns": lambda n : setattr(self, 'total_checkpoint_overhead_ns', n.get_int_value()),
            "total_checkpoint_storage_bytes": lambda n : setattr(self, 'total_checkpoint_storage_bytes', n.get_int_value()),
            "total_checkpoints": lambda n : setattr(self, 'total_checkpoints', n.get_int_value()),
            "total_estimated_savings": lambda n : setattr(self, 'total_estimated_savings', n.get_float_value()),
            "total_heartbeat_checkpoints": lambda n : setattr(self, 'total_heartbeat_checkpoints', n.get_int_value()),
            "total_manual_checkpoints": lambda n : setattr(self, 'total_manual_checkpoints', n.get_int_value()),
            "total_time_protected_seconds": lambda n : setattr(self, 'total_time_protected_seconds', n.get_float_value()),
            "worst_case_recovery_point_seconds": lambda n : setattr(self, 'worst_case_recovery_point_seconds', n.get_float_value()),
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
        writer.write_float_value("avg_checkpoint_interval_seconds", self.avg_checkpoint_interval_seconds)
        writer.write_int_value("pods_protected", self.pods_protected)
        writer.write_datetime_value("refreshed_at", self.refreshed_at)
        writer.write_int_value("total_checkpoint_overhead_ns", self.total_checkpoint_overhead_ns)
        writer.write_int_value("total_checkpoint_storage_bytes", self.total_checkpoint_storage_bytes)
        writer.write_int_value("total_checkpoints", self.total_checkpoints)
        writer.write_float_value("total_estimated_savings", self.total_estimated_savings)
        writer.write_int_value("total_heartbeat_checkpoints", self.total_heartbeat_checkpoints)
        writer.write_int_value("total_manual_checkpoints", self.total_manual_checkpoints)
        writer.write_float_value("total_time_protected_seconds", self.total_time_protected_seconds)
        writer.write_float_value("worst_case_recovery_point_seconds", self.worst_case_recovery_point_seconds)
        writer.write_additional_data_value(self.additional_data)
    

