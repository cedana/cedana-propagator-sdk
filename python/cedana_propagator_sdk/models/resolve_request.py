from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .resolve_request_active_streams_by_profile import ResolveRequest_active_streams_by_profile

@dataclass
class ResolveRequest(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The active_streams_by_profile property
    active_streams_by_profile: Optional[ResolveRequest_active_streams_by_profile] = None
    # The authorization_id property
    authorization_id: Optional[UUID] = None
    # The lifetime_protocol property
    lifetime_protocol: Optional[int] = None
    # The logical_model property
    logical_model: Optional[str] = None
    # The preferred_profile_id property
    preferred_profile_id: Optional[str] = None
    # The request_id property
    request_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ResolveRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ResolveRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ResolveRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .resolve_request_active_streams_by_profile import ResolveRequest_active_streams_by_profile

        from .resolve_request_active_streams_by_profile import ResolveRequest_active_streams_by_profile

        fields: dict[str, Callable[[Any], None]] = {
            "active_streams_by_profile": lambda n : setattr(self, 'active_streams_by_profile', n.get_object_value(ResolveRequest_active_streams_by_profile)),
            "authorization_id": lambda n : setattr(self, 'authorization_id', n.get_uuid_value()),
            "lifetime_protocol": lambda n : setattr(self, 'lifetime_protocol', n.get_int_value()),
            "logical_model": lambda n : setattr(self, 'logical_model', n.get_str_value()),
            "preferred_profile_id": lambda n : setattr(self, 'preferred_profile_id', n.get_str_value()),
            "request_id": lambda n : setattr(self, 'request_id', n.get_str_value()),
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
        writer.write_object_value("active_streams_by_profile", self.active_streams_by_profile)
        writer.write_uuid_value("authorization_id", self.authorization_id)
        writer.write_int_value("lifetime_protocol", self.lifetime_protocol)
        writer.write_str_value("logical_model", self.logical_model)
        writer.write_str_value("preferred_profile_id", self.preferred_profile_id)
        writer.write_str_value("request_id", self.request_id)
        writer.write_additional_data_value(self.additional_data)
    

