from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .slo_override import SloOverride
    from .slo_thresholds import SloThresholds

@dataclass
class SloConfig(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The org default; code defaults until one is saved.
    default: Optional[SloThresholds] = None
    # The overrides property
    overrides: Optional[list[SloOverride]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SloConfig:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SloConfig
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SloConfig()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .slo_override import SloOverride
        from .slo_thresholds import SloThresholds

        from .slo_override import SloOverride
        from .slo_thresholds import SloThresholds

        fields: dict[str, Callable[[Any], None]] = {
            "default": lambda n : setattr(self, 'default', n.get_object_value(SloThresholds)),
            "overrides": lambda n : setattr(self, 'overrides', n.get_collection_of_object_values(SloOverride)),
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
        writer.write_object_value("default", self.default)
        writer.write_collection_of_object_values("overrides", self.overrides)
        writer.write_additional_data_value(self.additional_data)
    

