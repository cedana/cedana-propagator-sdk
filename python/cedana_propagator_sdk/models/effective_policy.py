from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .priority import Priority
    from .schedule_window import ScheduleWindow
    from .sources import Sources

@dataclass
class EffectivePolicy(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The idle_seconds property
    idle_seconds: Optional[int] = None
    # The max_replicas property
    max_replicas: Optional[int] = None
    # The min_replicas property
    min_replicas: Optional[int] = None
    # The never_park property
    never_park: Optional[bool] = None
    # The priority property
    priority: Optional[Priority] = None
    # The schedules property
    schedules: Optional[list[ScheduleWindow]] = None
    # The sources property
    sources: Optional[Sources] = None
    # The team property
    team: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EffectivePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EffectivePolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EffectivePolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .priority import Priority
        from .schedule_window import ScheduleWindow
        from .sources import Sources

        from .priority import Priority
        from .schedule_window import ScheduleWindow
        from .sources import Sources

        fields: dict[str, Callable[[Any], None]] = {
            "idle_seconds": lambda n : setattr(self, 'idle_seconds', n.get_int_value()),
            "max_replicas": lambda n : setattr(self, 'max_replicas', n.get_int_value()),
            "min_replicas": lambda n : setattr(self, 'min_replicas', n.get_int_value()),
            "never_park": lambda n : setattr(self, 'never_park', n.get_bool_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_enum_value(Priority)),
            "schedules": lambda n : setattr(self, 'schedules', n.get_collection_of_object_values(ScheduleWindow)),
            "sources": lambda n : setattr(self, 'sources', n.get_object_value(Sources)),
            "team": lambda n : setattr(self, 'team', n.get_str_value()),
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
        writer.write_int_value("idle_seconds", self.idle_seconds)
        writer.write_int_value("max_replicas", self.max_replicas)
        writer.write_int_value("min_replicas", self.min_replicas)
        writer.write_bool_value("never_park", self.never_park)
        writer.write_enum_value("priority", self.priority)
        writer.write_collection_of_object_values("schedules", self.schedules)
        writer.write_object_value("sources", self.sources)
        writer.write_str_value("team", self.team)
        writer.write_additional_data_value(self.additional_data)
    

