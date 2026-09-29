from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Residency(AdditionalDataHolder, Parsable):
    """
    Where a checkpoint currently lives. `node_name` is empty for NFS, which every node shares.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The bytes property
    bytes: Optional[int] = None
    # The node_name property
    node_name: Optional[str] = None
    # The since_ms property
    since_ms: Optional[int] = None
    # writing | persisting | copying | present
    state: Optional[str] = None
    # The tier property
    tier: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Residency:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Residency
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Residency()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "bytes": lambda n : setattr(self, 'bytes', n.get_int_value()),
            "node_name": lambda n : setattr(self, 'node_name', n.get_str_value()),
            "since_ms": lambda n : setattr(self, 'since_ms', n.get_int_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "tier": lambda n : setattr(self, 'tier', n.get_str_value()),
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
        writer.write_str_value("node_name", self.node_name)
        writer.write_int_value("since_ms", self.since_ms)
        writer.write_str_value("state", self.state)
        writer.write_str_value("tier", self.tier)
        writer.write_additional_data_value(self.additional_data)
    

