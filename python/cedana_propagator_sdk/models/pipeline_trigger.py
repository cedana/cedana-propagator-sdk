from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .pipeline_trigger_member1 import PipelineTriggerMember1
    from .pipeline_trigger_member2 import PipelineTriggerMember2

@dataclass
class PipelineTrigger(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes PipelineTriggerMember1, PipelineTriggerMember2
    """
    # Composed type representation for type PipelineTriggerMember1
    pipeline_trigger_member1: Optional[PipelineTriggerMember1] = None
    # Composed type representation for type PipelineTriggerMember2
    pipeline_trigger_member2: Optional[PipelineTriggerMember2] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PipelineTrigger:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PipelineTrigger
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        result = PipelineTrigger()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .pipeline_trigger_member1 import PipelineTriggerMember1
        from .pipeline_trigger_member2 import PipelineTriggerMember2

        if self.pipeline_trigger_member1:
            return self.pipeline_trigger_member1.get_field_deserializers()
        if self.pipeline_trigger_member2:
            return self.pipeline_trigger_member2.get_field_deserializers()
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        if self.pipeline_trigger_member1:
            writer.write_object_value(None, self.pipeline_trigger_member1)
        elif self.pipeline_trigger_member2:
            writer.write_object_value(None, self.pipeline_trigger_member2)
    

