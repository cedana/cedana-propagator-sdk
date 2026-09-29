from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .notification_event import NotificationEvent
    from .residency import Residency

@dataclass
class CheckpointStorage(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The checkpoint_id property
    checkpoint_id: Optional[str] = None
    # Checkpoint, restore and CSX storage events for this checkpoint, oldest first.
    events: Optional[list[NotificationEvent]] = None
    # Where the checkpoint lives now, per node and tier.
    residency: Optional[list[Residency]] = None
    # More events exist than were returned; only the newest are included.
    truncated: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CheckpointStorage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CheckpointStorage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CheckpointStorage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .notification_event import NotificationEvent
        from .residency import Residency

        from .notification_event import NotificationEvent
        from .residency import Residency

        fields: dict[str, Callable[[Any], None]] = {
            "checkpoint_id": lambda n : setattr(self, 'checkpoint_id', n.get_str_value()),
            "events": lambda n : setattr(self, 'events', n.get_collection_of_object_values(NotificationEvent)),
            "residency": lambda n : setattr(self, 'residency', n.get_collection_of_object_values(Residency)),
            "truncated": lambda n : setattr(self, 'truncated', n.get_bool_value()),
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
        writer.write_str_value("checkpoint_id", self.checkpoint_id)
        writer.write_collection_of_object_values("events", self.events)
        writer.write_collection_of_object_values("residency", self.residency)
        writer.write_bool_value("truncated", self.truncated)
        writer.write_additional_data_value(self.additional_data)
    

