from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .maintenance_trigger_config import MaintenanceTriggerConfig
    from .pipeline_trigger_member2_type import PipelineTriggerMember2_type

@dataclass
class PipelineTriggerMember2(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The config property
    config: Optional[MaintenanceTriggerConfig] = None
    # The type property
    type: Optional[PipelineTriggerMember2_type] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PipelineTriggerMember2:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PipelineTriggerMember2
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PipelineTriggerMember2()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .maintenance_trigger_config import MaintenanceTriggerConfig
        from .pipeline_trigger_member2_type import PipelineTriggerMember2_type

        from .maintenance_trigger_config import MaintenanceTriggerConfig
        from .pipeline_trigger_member2_type import PipelineTriggerMember2_type

        fields: dict[str, Callable[[Any], None]] = {
            "config": lambda n : setattr(self, 'config', n.get_object_value(MaintenanceTriggerConfig)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(PipelineTriggerMember2_type)),
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
    

