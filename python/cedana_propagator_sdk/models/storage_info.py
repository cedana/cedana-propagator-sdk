from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class StorageInfo(AdditionalDataHolder, Parsable):
    """
    Local storage of one node.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Ephemeral storage the scheduler can hand out, after system reservations
    allocatable_ephemeral_storage_bytes: Optional[int] = None
    # CSI drivers serving the node, from their topology labels, e.g. ["csi.weka.io"]
    csi_drivers: Optional[list[str]] = None
    # The ephemeral_storage_bytes property
    ephemeral_storage_bytes: Optional[int] = None
    # Whether the node has a non-rotational (SSD/NVMe) disk (Node Feature Discovery)
    local_ssd: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StorageInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StorageInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StorageInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "allocatable_ephemeral_storage_bytes": lambda n : setattr(self, 'allocatable_ephemeral_storage_bytes', n.get_int_value()),
            "csi_drivers": lambda n : setattr(self, 'csi_drivers', n.get_collection_of_primitive_values(str)),
            "ephemeral_storage_bytes": lambda n : setattr(self, 'ephemeral_storage_bytes', n.get_int_value()),
            "local_ssd": lambda n : setattr(self, 'local_ssd', n.get_bool_value()),
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
        writer.write_int_value("allocatable_ephemeral_storage_bytes", self.allocatable_ephemeral_storage_bytes)
        writer.write_collection_of_primitive_values("csi_drivers", self.csi_drivers)
        writer.write_int_value("ephemeral_storage_bytes", self.ephemeral_storage_bytes)
        writer.write_bool_value("local_ssd", self.local_ssd)
        writer.write_additional_data_value(self.additional_data)
    

