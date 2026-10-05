from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DispatchHoldOutcomes(AdditionalDataHolder, Parsable):
    """
    What became of the requests that were parked: the restore-versus-coldpayoff, measured on the requests that waited for it.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Wait from first park to assignment, over the requests that were served.
    avg_wait_ms: Optional[float] = None
    # The held property
    held: Optional[int] = None
    # The later_served property
    later_served: Optional[int] = None
    # The max_wait_ms property
    max_wait_ms: Optional[float] = None
    # The served_after_cold_start property
    served_after_cold_start: Optional[int] = None
    # The served_after_restore property
    served_after_restore: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DispatchHoldOutcomes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DispatchHoldOutcomes
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DispatchHoldOutcomes()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "avg_wait_ms": lambda n : setattr(self, 'avg_wait_ms', n.get_float_value()),
            "held": lambda n : setattr(self, 'held', n.get_int_value()),
            "later_served": lambda n : setattr(self, 'later_served', n.get_int_value()),
            "max_wait_ms": lambda n : setattr(self, 'max_wait_ms', n.get_float_value()),
            "served_after_cold_start": lambda n : setattr(self, 'served_after_cold_start', n.get_int_value()),
            "served_after_restore": lambda n : setattr(self, 'served_after_restore', n.get_int_value()),
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
        writer.write_float_value("avg_wait_ms", self.avg_wait_ms)
        writer.write_int_value("held", self.held)
        writer.write_int_value("later_served", self.later_served)
        writer.write_float_value("max_wait_ms", self.max_wait_ms)
        writer.write_int_value("served_after_cold_start", self.served_after_cold_start)
        writer.write_int_value("served_after_restore", self.served_after_restore)
        writer.write_additional_data_value(self.additional_data)
    

