from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .placement_profile import PlacementProfile

@dataclass
class PlacementView(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The cluster placement resolved for inference, from lifecycle events. None untilsomething has run.
    cluster_id: Optional[UUID] = None
    # Allocatable GPUs on that cluster's Ready, schedulable nodes. None when unknown, inwhich case preemption falls back to displacing one victim.
    gpu_capacity: Optional[int] = None
    # GPUs held by resident or activating profiles on that cluster.
    occupied_gpus: Optional[int] = None
    # The profiles property
    profiles: Optional[list[PlacementProfile]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlacementView:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlacementView
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlacementView()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .placement_profile import PlacementProfile

        from .placement_profile import PlacementProfile

        fields: dict[str, Callable[[Any], None]] = {
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_uuid_value()),
            "gpu_capacity": lambda n : setattr(self, 'gpu_capacity', n.get_int_value()),
            "occupied_gpus": lambda n : setattr(self, 'occupied_gpus', n.get_int_value()),
            "profiles": lambda n : setattr(self, 'profiles', n.get_collection_of_object_values(PlacementProfile)),
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
        writer.write_int_value("gpu_capacity", self.gpu_capacity)
        writer.write_int_value("occupied_gpus", self.occupied_gpus)
        writer.write_collection_of_object_values("profiles", self.profiles)
        writer.write_additional_data_value(self.additional_data)
    

