from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.telemetry_record import TelemetryRecord

@dataclass
class TelemetryBody(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes list[TelemetryRecord], TelemetryRecord
    """
    # Composed type representation for type TelemetryRecord
    telemetry_body_telemetry_record: Optional[TelemetryRecord] = None
    # Composed type representation for type list[TelemetryRecord]
    telemetry_record: Optional[list[TelemetryRecord]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TelemetryBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TelemetryBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        result = TelemetryBody()
        if mapping_value and mapping_value.casefold() == "TelemetryRecord".casefold():
            from .....models.telemetry_record import TelemetryRecord

            result.telemetry_body_telemetry_record = TelemetryRecord()
        elif telemetry_record_value := parse_node.get_collection_of_object_values(TelemetryRecord):
            result.telemetry_record = telemetry_record_value
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....models.telemetry_record import TelemetryRecord

        if self.telemetry_body_telemetry_record:
            return self.telemetry_body_telemetry_record.get_field_deserializers()
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        if self.telemetry_body_telemetry_record:
            writer.write_object_value(None, self.telemetry_body_telemetry_record)
        elif self.telemetry_record:
            writer.write_collection_of_object_values(None, self.telemetry_record)
    

