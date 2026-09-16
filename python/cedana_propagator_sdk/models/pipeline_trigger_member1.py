from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .heartbeat_trigger_config import HeartbeatTriggerConfig
    from .pipeline_trigger_member1_type import PipelineTriggerMember1_type

@dataclass
class PipelineTriggerMember1(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The config property
    config: Optional[HeartbeatTriggerConfig] = None
    # The type property
    type: Optional[PipelineTriggerMember1_type] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PipelineTriggerMember1:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PipelineTriggerMember1
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PipelineTriggerMember1()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .heartbeat_trigger_config import HeartbeatTriggerConfig
        from .pipeline_trigger_member1_type import PipelineTriggerMember1_type

        from .heartbeat_trigger_config import HeartbeatTriggerConfig
        from .pipeline_trigger_member1_type import PipelineTriggerMember1_type

        fields: dict[str, Callable[[Any], None]] = {
            "config": lambda n : setattr(self, 'config', n.get_object_value(HeartbeatTriggerConfig)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(PipelineTriggerMember1_type)),
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
        writer.write_object_value("config", self.config)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

