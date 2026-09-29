from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .csx_checkpoint import CsxCheckpoint
    from .csx_node import CsxNode

@dataclass
class ClusterResidency(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Checkpoints that still live somewhere, newest first.
    checkpoints: Optional[list[CsxCheckpoint]] = None
    # The nfs_bytes property
    nfs_bytes: Optional[int] = None
    # The nfs_checkpoints property
    nfs_checkpoints: Optional[int] = None
    # The nodes property
    nodes: Optional[list[CsxNode]] = None
    # Only the newest storage rows were folded; older checkpoints may be missing.
    truncated: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ClusterResidency:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ClusterResidency
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ClusterResidency()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .csx_checkpoint import CsxCheckpoint
        from .csx_node import CsxNode

        from .csx_checkpoint import CsxCheckpoint
        from .csx_node import CsxNode

        fields: dict[str, Callable[[Any], None]] = {
            "checkpoints": lambda n : setattr(self, 'checkpoints', n.get_collection_of_object_values(CsxCheckpoint)),
            "nfs_bytes": lambda n : setattr(self, 'nfs_bytes', n.get_int_value()),
            "nfs_checkpoints": lambda n : setattr(self, 'nfs_checkpoints', n.get_int_value()),
            "nodes": lambda n : setattr(self, 'nodes', n.get_collection_of_object_values(CsxNode)),
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
        writer.write_collection_of_object_values("checkpoints", self.checkpoints)
        writer.write_int_value("nfs_bytes", self.nfs_bytes)
        writer.write_int_value("nfs_checkpoints", self.nfs_checkpoints)
        writer.write_collection_of_object_values("nodes", self.nodes)
        writer.write_bool_value("truncated", self.truncated)
        writer.write_additional_data_value(self.additional_data)
    

