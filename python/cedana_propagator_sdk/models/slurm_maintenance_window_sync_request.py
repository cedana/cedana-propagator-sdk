from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .slurm_maintenance_window_sync import SlurmMaintenanceWindowSync

@dataclass
class SlurmMaintenanceWindowSyncRequest(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The cluster_id property
    cluster_id: Optional[UUID] = None
    # The maintenance_windows property
    maintenance_windows: Optional[list[SlurmMaintenanceWindowSync]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SlurmMaintenanceWindowSyncRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SlurmMaintenanceWindowSyncRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SlurmMaintenanceWindowSyncRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .slurm_maintenance_window_sync import SlurmMaintenanceWindowSync

        from .slurm_maintenance_window_sync import SlurmMaintenanceWindowSync

        fields: dict[str, Callable[[Any], None]] = {
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_uuid_value()),
            "maintenance_windows": lambda n : setattr(self, 'maintenance_windows', n.get_collection_of_object_values(SlurmMaintenanceWindowSync)),
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
        writer.write_uuid_value("cluster_id", self.cluster_id)
        writer.write_collection_of_object_values("maintenance_windows", self.maintenance_windows)
        writer.write_additional_data_value(self.additional_data)
    

