from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DispatchWindow(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The from property
    from_: Optional[datetime.datetime] = None
    # The minutes property
    minutes: Optional[int] = None
    # The to property
    to: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DispatchWindow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DispatchWindow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DispatchWindow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "from": lambda n : setattr(self, 'from_', n.get_datetime_value()),
            "minutes": lambda n : setattr(self, 'minutes', n.get_int_value()),
            "to": lambda n : setattr(self, 'to', n.get_datetime_value()),
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
        writer.write_datetime_value("from", self.from_)
        writer.write_int_value("minutes", self.minutes)
        writer.write_datetime_value("to", self.to)
        writer.write_additional_data_value(self.additional_data)
    

