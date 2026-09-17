from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ResolveResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The activation_path property
    activation_path: Optional[str] = None
    # The decision_source property
    decision_source: Optional[str] = None
    # The fallback_used property
    fallback_used: Optional[bool] = None
    # The lease_duration_ms property
    lease_duration_ms: Optional[int] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # The route_generation property
    route_generation: Optional[int] = None
    # The target_name property
    target_name: Optional[str] = None
    # The upstream_model property
    upstream_model: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ResolveResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ResolveResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ResolveResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "activation_path": lambda n : setattr(self, 'activation_path', n.get_str_value()),
            "decision_source": lambda n : setattr(self, 'decision_source', n.get_str_value()),
            "fallback_used": lambda n : setattr(self, 'fallback_used', n.get_bool_value()),
            "lease_duration_ms": lambda n : setattr(self, 'lease_duration_ms', n.get_int_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "route_generation": lambda n : setattr(self, 'route_generation', n.get_int_value()),
            "target_name": lambda n : setattr(self, 'target_name', n.get_str_value()),
            "upstream_model": lambda n : setattr(self, 'upstream_model', n.get_str_value()),
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
        writer.write_str_value("activation_path", self.activation_path)
        writer.write_str_value("decision_source", self.decision_source)
        writer.write_bool_value("fallback_used", self.fallback_used)
        writer.write_int_value("lease_duration_ms", self.lease_duration_ms)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_int_value("route_generation", self.route_generation)
        writer.write_str_value("target_name", self.target_name)
        writer.write_str_value("upstream_model", self.upstream_model)
        writer.write_additional_data_value(self.additional_data)
    

