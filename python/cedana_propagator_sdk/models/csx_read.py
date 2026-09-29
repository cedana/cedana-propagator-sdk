from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CsxRead(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The at_ms property
    at_ms: Optional[int] = None
    # The duration_ns property
    duration_ns: Optional[int] = None
    # The node_name property
    node_name: Optional[str] = None
    # The tier property
    tier: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CsxRead:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CsxRead
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CsxRead()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "at_ms": lambda n : setattr(self, 'at_ms', n.get_int_value()),
            "duration_ns": lambda n : setattr(self, 'duration_ns', n.get_int_value()),
            "node_name": lambda n : setattr(self, 'node_name', n.get_str_value()),
            "tier": lambda n : setattr(self, 'tier', n.get_str_value()),
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
        writer.write_int_value("at_ms", self.at_ms)
        writer.write_int_value("duration_ns", self.duration_ns)
        writer.write_str_value("node_name", self.node_name)
        writer.write_str_value("tier", self.tier)
        writer.write_additional_data_value(self.additional_data)
    

