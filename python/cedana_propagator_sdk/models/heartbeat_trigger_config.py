from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class HeartbeatTriggerConfig(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The interval_seconds property
    interval_seconds: Optional[int] = None
    # Cap on successful checkpoints before auto-disable. Absent = run forever;when present must be `> 0` (rejected with 400 at creation, not stored).`i32` (not u32) bounds an oversized value at deserialization; matches cedana-ui.
    max_checkpoints: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HeartbeatTriggerConfig:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HeartbeatTriggerConfig
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HeartbeatTriggerConfig()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "interval_seconds": lambda n : setattr(self, 'interval_seconds', n.get_int_value()),
            "max_checkpoints": lambda n : setattr(self, 'max_checkpoints', n.get_int_value()),
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
        writer.write_int_value("interval_seconds", self.interval_seconds)
        writer.write_int_value("max_checkpoints", self.max_checkpoints)
        writer.write_additional_data_value(self.additional_data)
    

