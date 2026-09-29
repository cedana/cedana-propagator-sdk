from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CsxNode(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The disk_checkpoints property
    disk_checkpoints: Optional[int] = None
    # The disk_limit_bytes property
    disk_limit_bytes: Optional[int] = None
    # The disk_used_bytes property
    disk_used_bytes: Optional[int] = None
    # The memory_checkpoints property
    memory_checkpoints: Optional[int] = None
    # The memory_limit_bytes property
    memory_limit_bytes: Optional[int] = None
    # Includes copies in flight, which CSX reserves up front.
    memory_used_bytes: Optional[int] = None
    # The node_name property
    node_name: Optional[str] = None
    # Last CSX start; the node's caches were empty then.
    started_ms: Optional[int] = None
    # The version property
    version: Optional[str] = None
    # Bytes of finished writes still in the tmpfs buffer, waiting to be persisted to NFS.
    write_buffer_bytes: Optional[int] = None
    # The writes_in_flight property
    writes_in_flight: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CsxNode:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CsxNode
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CsxNode()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "disk_checkpoints": lambda n : setattr(self, 'disk_checkpoints', n.get_int_value()),
            "disk_limit_bytes": lambda n : setattr(self, 'disk_limit_bytes', n.get_int_value()),
            "disk_used_bytes": lambda n : setattr(self, 'disk_used_bytes', n.get_int_value()),
            "memory_checkpoints": lambda n : setattr(self, 'memory_checkpoints', n.get_int_value()),
            "memory_limit_bytes": lambda n : setattr(self, 'memory_limit_bytes', n.get_int_value()),
            "memory_used_bytes": lambda n : setattr(self, 'memory_used_bytes', n.get_int_value()),
            "node_name": lambda n : setattr(self, 'node_name', n.get_str_value()),
            "started_ms": lambda n : setattr(self, 'started_ms', n.get_int_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
            "write_buffer_bytes": lambda n : setattr(self, 'write_buffer_bytes', n.get_int_value()),
            "writes_in_flight": lambda n : setattr(self, 'writes_in_flight', n.get_int_value()),
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
        writer.write_int_value("disk_checkpoints", self.disk_checkpoints)
        writer.write_int_value("disk_limit_bytes", self.disk_limit_bytes)
        writer.write_int_value("disk_used_bytes", self.disk_used_bytes)
        writer.write_int_value("memory_checkpoints", self.memory_checkpoints)
        writer.write_int_value("memory_limit_bytes", self.memory_limit_bytes)
        writer.write_int_value("memory_used_bytes", self.memory_used_bytes)
        writer.write_str_value("node_name", self.node_name)
        writer.write_int_value("started_ms", self.started_ms)
        writer.write_str_value("version", self.version)
        writer.write_int_value("write_buffer_bytes", self.write_buffer_bytes)
        writer.write_int_value("writes_in_flight", self.writes_in_flight)
        writer.write_additional_data_value(self.additional_data)
    

