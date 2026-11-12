from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class AuthorizeResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The authorization_id property
    authorization_id: Optional[UUID] = None
    # The gateway may reuse this decision briefly: true only for keys with no rate limit orbudget, which are charged on every authorize.
    cacheable: Optional[bool] = None
    # The expires_at property
    expires_at: Optional[datetime.datetime] = None
    # The key the caller presented; the gateway echoes it in telemetry so usage keeps itfor requests served from its authorization cache.
    key_id: Optional[str] = None
    # The route_generation property
    route_generation: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthorizeResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthorizeResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthorizeResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "authorization_id": lambda n : setattr(self, 'authorization_id', n.get_uuid_value()),
            "cacheable": lambda n : setattr(self, 'cacheable', n.get_bool_value()),
            "expires_at": lambda n : setattr(self, 'expires_at', n.get_datetime_value()),
            "key_id": lambda n : setattr(self, 'key_id', n.get_str_value()),
            "route_generation": lambda n : setattr(self, 'route_generation', n.get_int_value()),
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
        writer.write_uuid_value("authorization_id", self.authorization_id)
        writer.write_bool_value("cacheable", self.cacheable)
        writer.write_datetime_value("expires_at", self.expires_at)
        writer.write_str_value("key_id", self.key_id)
        writer.write_int_value("route_generation", self.route_generation)
        writer.write_additional_data_value(self.additional_data)
    

