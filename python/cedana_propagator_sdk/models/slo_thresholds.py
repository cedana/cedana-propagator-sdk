from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SloThresholds(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Fraction of requests, 0 to 1.
    error_rate: Optional[float] = None
    # The inter_token_p95_ms property
    inter_token_p95_ms: Optional[float] = None
    # The ttft_p95_ms property
    ttft_p95_ms: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SloThresholds:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SloThresholds
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SloThresholds()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "error_rate": lambda n : setattr(self, 'error_rate', n.get_float_value()),
            "inter_token_p95_ms": lambda n : setattr(self, 'inter_token_p95_ms', n.get_float_value()),
            "ttft_p95_ms": lambda n : setattr(self, 'ttft_p95_ms', n.get_float_value()),
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
        writer.write_float_value("error_rate", self.error_rate)
        writer.write_float_value("inter_token_p95_ms", self.inter_token_p95_ms)
        writer.write_float_value("ttft_p95_ms", self.ttft_p95_ms)
        writer.write_additional_data_value(self.additional_data)
    

