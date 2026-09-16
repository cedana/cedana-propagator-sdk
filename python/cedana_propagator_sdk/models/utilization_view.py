from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .profile_utilization import ProfileUtilization

@dataclass
class UtilizationView(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The cluster_id property
    cluster_id: Optional[UUID] = None
    # The gpu_capacity property
    gpu_capacity: Optional[int] = None
    # gpu_capacity x window, when capacity is known.
    gpu_seconds_available: Optional[float] = None
    # Sum over profiles of resident seconds x GPUs.
    gpu_seconds_resident: Optional[float] = None
    # The profiles property
    profiles: Optional[list[ProfileUtilization]] = None
    # Activations that completed inside the window (route publications).
    swaps: Optional[int] = None
    # gpu_seconds_resident / gpu_seconds_available; the number to set beside anenterprise fleet's 15-22%. Residency of a serving model, not SM occupancy.
    utilization: Optional[float] = None
    # The window_hours property
    window_hours: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UtilizationView:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UtilizationView
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UtilizationView()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .profile_utilization import ProfileUtilization

        from .profile_utilization import ProfileUtilization

        fields: dict[str, Callable[[Any], None]] = {
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_uuid_value()),
            "gpu_capacity": lambda n : setattr(self, 'gpu_capacity', n.get_int_value()),
            "gpu_seconds_available": lambda n : setattr(self, 'gpu_seconds_available', n.get_float_value()),
            "gpu_seconds_resident": lambda n : setattr(self, 'gpu_seconds_resident', n.get_float_value()),
            "profiles": lambda n : setattr(self, 'profiles', n.get_collection_of_object_values(ProfileUtilization)),
            "swaps": lambda n : setattr(self, 'swaps', n.get_int_value()),
            "utilization": lambda n : setattr(self, 'utilization', n.get_float_value()),
            "window_hours": lambda n : setattr(self, 'window_hours', n.get_float_value()),
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
        writer.write_float_value("gpu_seconds_available", self.gpu_seconds_available)
        writer.write_float_value("gpu_seconds_resident", self.gpu_seconds_resident)
        writer.write_collection_of_object_values("profiles", self.profiles)
        writer.write_int_value("swaps", self.swaps)
        writer.write_float_value("utilization", self.utilization)
        writer.write_float_value("window_hours", self.window_hours)
        writer.write_additional_data_value(self.additional_data)
    

