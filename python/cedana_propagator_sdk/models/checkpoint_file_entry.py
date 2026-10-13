from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CheckpointFileEntry(AdditionalDataHolder, Parsable):
    """
    A file inside a checkpoint: an archive member, or a child of a checkpoint directory
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The is_dir property
    is_dir: Optional[bool] = None
    # Modification time, Unix ms
    mod_time: Optional[int] = None
    # The name property
    name: Optional[str] = None
    # Size in bytes
    size: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CheckpointFileEntry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CheckpointFileEntry
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CheckpointFileEntry()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "is_dir": lambda n : setattr(self, 'is_dir', n.get_bool_value()),
            "mod_time": lambda n : setattr(self, 'mod_time', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
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
        writer.write_bool_value("is_dir", self.is_dir)
        writer.write_int_value("mod_time", self.mod_time)
        writer.write_str_value("name", self.name)
        writer.write_int_value("size", self.size)
        writer.write_additional_data_value(self.additional_data)
    

