from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WorkerStart(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The checkpoint_path property
    checkpoint_path: Optional[str] = None
    # The pod_name property
    pod_name: Optional[str] = None
    # The ready_at property
    ready_at: Optional[datetime.datetime] = None
    # True when a restore is bound to this worker pod.
    restored: Optional[bool] = None
    # PodScheduled to Ready, in milliseconds.
    start_time_ms: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkerStart:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkerStart
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkerStart()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "checkpoint_path": lambda n : setattr(self, 'checkpoint_path', n.get_str_value()),
            "pod_name": lambda n : setattr(self, 'pod_name', n.get_str_value()),
            "ready_at": lambda n : setattr(self, 'ready_at', n.get_datetime_value()),
            "restored": lambda n : setattr(self, 'restored', n.get_bool_value()),
            "start_time_ms": lambda n : setattr(self, 'start_time_ms', n.get_int_value()),
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
        writer.write_str_value("checkpoint_path", self.checkpoint_path)
        writer.write_str_value("pod_name", self.pod_name)
        writer.write_datetime_value("ready_at", self.ready_at)
        writer.write_bool_value("restored", self.restored)
        writer.write_int_value("start_time_ms", self.start_time_ms)
        writer.write_additional_data_value(self.additional_data)
    

