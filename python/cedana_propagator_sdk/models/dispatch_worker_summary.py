from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DispatchWorkerSummary(AdditionalDataHolder, Parsable):
    """
    Per worker pod: what it served, and whether it was a restore.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The assigned property
    assigned: Optional[int] = None
    # The avg_ttft_ms property
    avg_ttft_ms: Optional[float] = None
    # The cached_tokens property
    cached_tokens: Optional[int] = None
    # The completed property
    completed: Optional[int] = None
    # The last_dispatch_at property
    last_dispatch_at: Optional[datetime.datetime] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # The worker_checkpoint_path property
    worker_checkpoint_path: Optional[str] = None
    # The worker_node_name property
    worker_node_name: Optional[str] = None
    # The worker_pod_name property
    worker_pod_name: Optional[str] = None
    # The worker_start_kind property
    worker_start_kind: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DispatchWorkerSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DispatchWorkerSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DispatchWorkerSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "assigned": lambda n : setattr(self, 'assigned', n.get_int_value()),
            "avg_ttft_ms": lambda n : setattr(self, 'avg_ttft_ms', n.get_float_value()),
            "cached_tokens": lambda n : setattr(self, 'cached_tokens', n.get_int_value()),
            "completed": lambda n : setattr(self, 'completed', n.get_int_value()),
            "last_dispatch_at": lambda n : setattr(self, 'last_dispatch_at', n.get_datetime_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "worker_checkpoint_path": lambda n : setattr(self, 'worker_checkpoint_path', n.get_str_value()),
            "worker_node_name": lambda n : setattr(self, 'worker_node_name', n.get_str_value()),
            "worker_pod_name": lambda n : setattr(self, 'worker_pod_name', n.get_str_value()),
            "worker_start_kind": lambda n : setattr(self, 'worker_start_kind', n.get_str_value()),
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
        writer.write_int_value("assigned", self.assigned)
        writer.write_float_value("avg_ttft_ms", self.avg_ttft_ms)
        writer.write_int_value("cached_tokens", self.cached_tokens)
        writer.write_int_value("completed", self.completed)
        writer.write_datetime_value("last_dispatch_at", self.last_dispatch_at)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_str_value("worker_checkpoint_path", self.worker_checkpoint_path)
        writer.write_str_value("worker_node_name", self.worker_node_name)
        writer.write_str_value("worker_pod_name", self.worker_pod_name)
        writer.write_str_value("worker_start_kind", self.worker_start_kind)
        writer.write_additional_data_value(self.additional_data)
    

