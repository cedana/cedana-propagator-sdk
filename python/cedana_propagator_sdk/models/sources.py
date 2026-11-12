from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .source import Source

@dataclass
class Sources(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The idle_seconds property
    idle_seconds: Optional[Source] = None
    # The max_replicas property
    max_replicas: Optional[Source] = None
    # The min_replicas property
    min_replicas: Optional[Source] = None
    # The never_park property
    never_park: Optional[Source] = None
    # The priority property
    priority: Optional[Source] = None
    # The schedules property
    schedules: Optional[Source] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Sources:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Sources
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Sources()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .source import Source

        from .source import Source

        fields: dict[str, Callable[[Any], None]] = {
            "idle_seconds": lambda n : setattr(self, 'idle_seconds', n.get_enum_value(Source)),
            "max_replicas": lambda n : setattr(self, 'max_replicas', n.get_enum_value(Source)),
            "min_replicas": lambda n : setattr(self, 'min_replicas', n.get_enum_value(Source)),
            "never_park": lambda n : setattr(self, 'never_park', n.get_enum_value(Source)),
            "priority": lambda n : setattr(self, 'priority', n.get_enum_value(Source)),
            "schedules": lambda n : setattr(self, 'schedules', n.get_enum_value(Source)),
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
        writer.write_enum_value("idle_seconds", self.idle_seconds)
        writer.write_enum_value("max_replicas", self.max_replicas)
        writer.write_enum_value("min_replicas", self.min_replicas)
        writer.write_enum_value("never_park", self.never_park)
        writer.write_enum_value("priority", self.priority)
        writer.write_enum_value("schedules", self.schedules)
        writer.write_additional_data_value(self.additional_data)
    

