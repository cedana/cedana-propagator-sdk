from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SwitchCost(AdditionalDataHolder, Parsable):
    """
    What a switch actually costs this profile, from the cluster's own history.A scheduler cannot derive these: they need checkpoint history the substrateowns. `cold_start_s` is `Option` and never estimated -- an estimated cold startsilently becomes a claim, and the per-profile estimates proved to be 3xoptimistic for the 1-GPU models and pessimistic for devstral2.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The cold_start_observed_at property
    cold_start_observed_at: Optional[datetime.datetime] = None
    # Activate-to-ready with no checkpoint present, observed at mint time.None until this profile has been minted on this hardware.
    cold_start_s: Optional[float] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # Withdrawn -> published again for this profile. Every activation is arestore in a working system, so this is the cost an eviction decision pays.
    swap_p50_s: Optional[float] = None
    # The swap_p90_s property
    swap_p90_s: Optional[float] = None
    # The swaps_observed property
    swaps_observed: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SwitchCost:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SwitchCost
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SwitchCost()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "cold_start_observed_at": lambda n : setattr(self, 'cold_start_observed_at', n.get_datetime_value()),
            "cold_start_s": lambda n : setattr(self, 'cold_start_s', n.get_float_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "swap_p50_s": lambda n : setattr(self, 'swap_p50_s', n.get_float_value()),
            "swap_p90_s": lambda n : setattr(self, 'swap_p90_s', n.get_float_value()),
            "swaps_observed": lambda n : setattr(self, 'swaps_observed', n.get_int_value()),
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
        writer.write_datetime_value("cold_start_observed_at", self.cold_start_observed_at)
        writer.write_float_value("cold_start_s", self.cold_start_s)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_float_value("swap_p50_s", self.swap_p50_s)
        writer.write_float_value("swap_p90_s", self.swap_p90_s)
        writer.write_int_value("swaps_observed", self.swaps_observed)
        writer.write_additional_data_value(self.additional_data)
    

