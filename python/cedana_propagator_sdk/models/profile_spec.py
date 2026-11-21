from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .container_spec import ContainerSpec
    from .model_spec import ModelSpec

@dataclass
class ProfileSpec(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes ContainerSpec, ModelSpec
    """
    # Composed type representation for type ContainerSpec
    container_spec: Optional[ContainerSpec] = None
    # Composed type representation for type ModelSpec
    model_spec: Optional[ModelSpec] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProfileSpec:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProfileSpec
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        result = ProfileSpec()
        if mapping_value and mapping_value.casefold() == "ContainerSpec".casefold():
            from .container_spec import ContainerSpec

            result.container_spec = ContainerSpec()
        elif mapping_value and mapping_value.casefold() == "ModelSpec".casefold():
            from .model_spec import ModelSpec

            result.model_spec = ModelSpec()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .container_spec import ContainerSpec
        from .model_spec import ModelSpec

        if self.container_spec:
            return self.container_spec.get_field_deserializers()
        if self.model_spec:
            return self.model_spec.get_field_deserializers()
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        if self.container_spec:
            writer.write_object_value(None, self.container_spec)
        elif self.model_spec:
            writer.write_object_value(None, self.model_spec)
    

