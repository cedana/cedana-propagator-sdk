from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .create import Create
    from .pipeline_filter import PipelineFilter

@dataclass
class PolicyPipeline(AdditionalDataHolder, Parsable):
    """
    Complete policy pipeline definition
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Action defines WHAT to do when triggered
    action: Optional[Create] = None
    # Filter defines WHAT resources are targeted
    filter: Optional[PipelineFilter] = None
    # Trigger defines WHEN a policy activates
    trigger: Optional[Create] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyPipeline:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyPipeline
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PolicyPipeline()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .create import Create
        from .pipeline_filter import PipelineFilter

        from .create import Create
        from .pipeline_filter import PipelineFilter

        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_object_value(Create)),
            "filter": lambda n : setattr(self, 'filter', n.get_object_value(PipelineFilter)),
            "trigger": lambda n : setattr(self, 'trigger', n.get_object_value(Create)),
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
        writer.write_object_value("action", self.action)
        writer.write_object_value("filter", self.filter)
        writer.write_object_value("trigger", self.trigger)
        writer.write_additional_data_value(self.additional_data)
    

