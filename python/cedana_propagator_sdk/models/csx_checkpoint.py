from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .csx_read import CsxRead
    from .residency import Residency

@dataclass
class CsxCheckpoint(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The bytes property
    bytes: Optional[int] = None
    # The checkpoint_id property
    checkpoint_id: Optional[str] = None
    # The first_seen_ms property
    first_seen_ms: Optional[int] = None
    # The last_event_ms property
    last_event_ms: Optional[int] = None
    # The last_read property
    last_read: Optional[CsxRead] = None
    # The name property
    name: Optional[str] = None
    # The namespace property
    namespace: Optional[str] = None
    # The reads property
    reads: Optional[int] = None
    # The residency property
    residency: Optional[list[Residency]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CsxCheckpoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CsxCheckpoint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CsxCheckpoint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .csx_read import CsxRead
        from .residency import Residency

        from .csx_read import CsxRead
        from .residency import Residency

        fields: dict[str, Callable[[Any], None]] = {
            "bytes": lambda n : setattr(self, 'bytes', n.get_int_value()),
            "checkpoint_id": lambda n : setattr(self, 'checkpoint_id', n.get_str_value()),
            "first_seen_ms": lambda n : setattr(self, 'first_seen_ms', n.get_int_value()),
            "last_event_ms": lambda n : setattr(self, 'last_event_ms', n.get_int_value()),
            "last_read": lambda n : setattr(self, 'last_read', n.get_object_value(CsxRead)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "namespace": lambda n : setattr(self, 'namespace', n.get_str_value()),
            "reads": lambda n : setattr(self, 'reads', n.get_int_value()),
            "residency": lambda n : setattr(self, 'residency', n.get_collection_of_object_values(Residency)),
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
        writer.write_int_value("bytes", self.bytes)
        writer.write_str_value("checkpoint_id", self.checkpoint_id)
        writer.write_int_value("first_seen_ms", self.first_seen_ms)
        writer.write_int_value("last_event_ms", self.last_event_ms)
        writer.write_object_value("last_read", self.last_read)
        writer.write_str_value("name", self.name)
        writer.write_str_value("namespace", self.namespace)
        writer.write_int_value("reads", self.reads)
        writer.write_collection_of_object_values("residency", self.residency)
        writer.write_additional_data_value(self.additional_data)
    

