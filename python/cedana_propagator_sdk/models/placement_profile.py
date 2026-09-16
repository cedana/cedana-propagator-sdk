from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class PlacementProfile(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The activating property
    activating: Optional[bool] = None
    # The cluster_id property
    cluster_id: Optional[UUID] = None
    # The gpus property
    gpus: Optional[int] = None
    # The logical_model property
    logical_model: Optional[str] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # The resident property
    resident: Optional[bool] = None
    # The suspending property
    suspending: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlacementProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlacementProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlacementProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "activating": lambda n : setattr(self, 'activating', n.get_bool_value()),
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_uuid_value()),
            "gpus": lambda n : setattr(self, 'gpus', n.get_int_value()),
            "logical_model": lambda n : setattr(self, 'logical_model', n.get_str_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "resident": lambda n : setattr(self, 'resident', n.get_bool_value()),
            "suspending": lambda n : setattr(self, 'suspending', n.get_bool_value()),
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
        writer.write_bool_value("activating", self.activating)
        writer.write_uuid_value("cluster_id", self.cluster_id)
        writer.write_int_value("gpus", self.gpus)
        writer.write_str_value("logical_model", self.logical_model)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_bool_value("resident", self.resident)
        writer.write_bool_value("suspending", self.suspending)
        writer.write_additional_data_value(self.additional_data)
    

