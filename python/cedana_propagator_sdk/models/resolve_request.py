from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .prefix_fingerprint import PrefixFingerprint
    from .resolve_request_active_streams_by_profile import ResolveRequest_active_streams_by_profile

@dataclass
class ResolveRequest(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The active_streams_by_profile property
    active_streams_by_profile: Optional[ResolveRequest_active_streams_by_profile] = None
    # The authorization_id property
    authorization_id: Optional[UUID] = None
    # Switchyard's pre-routing reuse estimate against the preferred profile,in tokens, already quantized to that profile's block size.
    expected_reuse_tokens: Optional[int] = None
    # The logical_model property
    logical_model: Optional[str] = None
    # Why Switchyard preferred that profile: "kv_affinity" when thepreference came from expected prefix reuse rather than the classifier.
    preference_reason: Optional[str] = None
    # The preferred_profile_id property
    preferred_profile_id: Optional[str] = None
    # Cumulative prefix fingerprints of this request, longest last. Recordedas restore hints when nothing is ready, so artifact selection canprefer a checkpoint holding what the queue is waiting for.
    prefix_fingerprints: Optional[list[PrefixFingerprint]] = None
    # The queued_requests property
    queued_requests: Optional[int] = None
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
        from .prefix_fingerprint import PrefixFingerprint
        from .resolve_request_active_streams_by_profile import ResolveRequest_active_streams_by_profile

        from .prefix_fingerprint import PrefixFingerprint
        from .resolve_request_active_streams_by_profile import ResolveRequest_active_streams_by_profile

        fields: dict[str, Callable[[Any], None]] = {
            "active_streams_by_profile": lambda n : setattr(self, 'active_streams_by_profile', n.get_object_value(ResolveRequest_active_streams_by_profile)),
            "authorization_id": lambda n : setattr(self, 'authorization_id', n.get_uuid_value()),
            "expected_reuse_tokens": lambda n : setattr(self, 'expected_reuse_tokens', n.get_int_value()),
            "logical_model": lambda n : setattr(self, 'logical_model', n.get_str_value()),
            "preference_reason": lambda n : setattr(self, 'preference_reason', n.get_str_value()),
            "preferred_profile_id": lambda n : setattr(self, 'preferred_profile_id', n.get_str_value()),
            "prefix_fingerprints": lambda n : setattr(self, 'prefix_fingerprints', n.get_collection_of_object_values(PrefixFingerprint)),
            "queued_requests": lambda n : setattr(self, 'queued_requests', n.get_int_value()),
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
        writer.write_int_value("expected_reuse_tokens", self.expected_reuse_tokens)
        writer.write_str_value("logical_model", self.logical_model)
        writer.write_str_value("preference_reason", self.preference_reason)
        writer.write_str_value("preferred_profile_id", self.preferred_profile_id)
        writer.write_collection_of_object_values("prefix_fingerprints", self.prefix_fingerprints)
        writer.write_int_value("queued_requests", self.queued_requests)
        writer.write_str_value("request_id", self.request_id)
        writer.write_additional_data_value(self.additional_data)
    

