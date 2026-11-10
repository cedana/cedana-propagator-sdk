from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class InferenceEvent(AdditionalDataHolder, Parsable):
    """
    One entry of a model's timeline, merged from the tables that record it.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The at property
    at: Optional[datetime.datetime] = None
    # The detail property
    detail: Optional[str] = None
    # The duration_ms property
    duration_ms: Optional[int] = None
    # worker.restored, worker.cold_start, worker.terminated, restore.failed, restore.fallback,checkpoint.first_ready, checkpoint.failed, model.parked, model.woken, model.scaled, or alifecycle kind.
    kind: Optional[str] = None
    # The logical_model property
    logical_model: Optional[str] = None
    # The pod_name property
    pod_name: Optional[str] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # The severity property
    severity: Optional[str] = None
    # The table the event came from.
    source: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InferenceEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InferenceEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InferenceEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "at": lambda n : setattr(self, 'at', n.get_datetime_value()),
            "detail": lambda n : setattr(self, 'detail', n.get_str_value()),
            "duration_ms": lambda n : setattr(self, 'duration_ms', n.get_int_value()),
            "kind": lambda n : setattr(self, 'kind', n.get_str_value()),
            "logical_model": lambda n : setattr(self, 'logical_model', n.get_str_value()),
            "pod_name": lambda n : setattr(self, 'pod_name', n.get_str_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
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
        writer.write_datetime_value("at", self.at)
        writer.write_str_value("detail", self.detail)
        writer.write_int_value("duration_ms", self.duration_ms)
        writer.write_str_value("kind", self.kind)
        writer.write_str_value("logical_model", self.logical_model)
        writer.write_str_value("pod_name", self.pod_name)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_str_value("severity", self.severity)
        writer.write_str_value("source", self.source)
        writer.write_additional_data_value(self.additional_data)
    

