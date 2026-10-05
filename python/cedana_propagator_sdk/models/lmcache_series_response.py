from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lmcache_series import LmcacheSeries

@dataclass
class LmcacheSeriesResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The bucket_seconds property
    bucket_seconds: Optional[int] = None
    # Newest sample in the window, or null when the profile never reported LMCache.
    latest_ms: Optional[int] = None
    # The minutes property
    minutes: Optional[int] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # The series property
    series: Optional[list[LmcacheSeries]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LmcacheSeriesResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LmcacheSeriesResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LmcacheSeriesResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .lmcache_series import LmcacheSeries

        from .lmcache_series import LmcacheSeries

        fields: dict[str, Callable[[Any], None]] = {
            "bucket_seconds": lambda n : setattr(self, 'bucket_seconds', n.get_int_value()),
            "latest_ms": lambda n : setattr(self, 'latest_ms', n.get_int_value()),
            "minutes": lambda n : setattr(self, 'minutes', n.get_int_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "series": lambda n : setattr(self, 'series', n.get_collection_of_object_values(LmcacheSeries)),
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
        writer.write_int_value("bucket_seconds", self.bucket_seconds)
        writer.write_int_value("latest_ms", self.latest_ms)
        writer.write_int_value("minutes", self.minutes)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_collection_of_object_values("series", self.series)
        writer.write_additional_data_value(self.additional_data)
    

