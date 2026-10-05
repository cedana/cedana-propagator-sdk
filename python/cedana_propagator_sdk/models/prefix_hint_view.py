from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PrefixHintView(AdditionalDataHolder, Parsable):
    """
    One prefix a parked or served request carried, in Switchyard's fingerprintspace. Opaque to everything except set intersection.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The last_seen property
    last_seen: Optional[datetime.datetime] = None
    # How many parked requests carried this prefix. Always 1 on theserved-prefix inventory, which counts residency, not demand.
    parked_count: Optional[int] = None
    # The prefix_hash property
    prefix_hash: Optional[str] = None
    # The prefix_tokens property
    prefix_tokens: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrefixHintView:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrefixHintView
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrefixHintView()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "last_seen": lambda n : setattr(self, 'last_seen', n.get_datetime_value()),
            "parked_count": lambda n : setattr(self, 'parked_count', n.get_int_value()),
            "prefix_hash": lambda n : setattr(self, 'prefix_hash', n.get_str_value()),
            "prefix_tokens": lambda n : setattr(self, 'prefix_tokens', n.get_int_value()),
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
        writer.write_datetime_value("last_seen", self.last_seen)
        writer.write_int_value("parked_count", self.parked_count)
        writer.write_str_value("prefix_hash", self.prefix_hash)
        writer.write_int_value("prefix_tokens", self.prefix_tokens)
        writer.write_additional_data_value(self.additional_data)
    

