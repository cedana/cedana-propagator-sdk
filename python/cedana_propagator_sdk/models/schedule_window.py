from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ScheduleWindow(AdditionalDataHolder, Parsable):
    """
    Keeps at least `min_replicas` warm inside the window.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # ISO weekdays, 1 = Monday.
    days: Optional[list[int]] = None
    # The end property
    end: Optional[str] = None
    # The min_replicas property
    min_replicas: Optional[int] = None
    # "HH:MM" local time; an end at or before the start runs past midnight.
    start: Optional[str] = None
    # IANA name, e.g. "America/New_York".
    timezone: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ScheduleWindow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ScheduleWindow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ScheduleWindow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "days": lambda n : setattr(self, 'days', n.get_collection_of_primitive_values(int)),
            "end": lambda n : setattr(self, 'end', n.get_str_value()),
            "min_replicas": lambda n : setattr(self, 'min_replicas', n.get_int_value()),
            "start": lambda n : setattr(self, 'start', n.get_str_value()),
            "timezone": lambda n : setattr(self, 'timezone', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("days", self.days)
        writer.write_str_value("end", self.end)
        writer.write_int_value("min_replicas", self.min_replicas)
        writer.write_str_value("start", self.start)
        writer.write_str_value("timezone", self.timezone)
        writer.write_additional_data_value(self.additional_data)
    

