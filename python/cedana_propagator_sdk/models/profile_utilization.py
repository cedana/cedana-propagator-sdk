from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ProfileUtilization(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The gpus property
    gpus: Optional[int] = None
    # The logical_model property
    logical_model: Optional[str] = None
    # The mean_slice_s property
    mean_slice_s: Optional[float] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # Seconds a published route existed for the profile inside the window.
    resident_s: Optional[float] = None
    # Route publications inside the window: activations that completed.
    slices: Optional[int] = None
    # Median seconds the node spent switching before this profile served: its swapcost. Compare against a cold start for the same model.
    swap_p50_s: Optional[float] = None
    # 90th percentile of the same, so a regression is visible rather than averaged out.
    swap_p90_s: Optional[float] = None
    # Swaps into this profile that were measured (the node was empty beforehand).
    swaps_measured: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProfileUtilization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProfileUtilization
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProfileUtilization()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "gpus": lambda n : setattr(self, 'gpus', n.get_int_value()),
            "logical_model": lambda n : setattr(self, 'logical_model', n.get_str_value()),
            "mean_slice_s": lambda n : setattr(self, 'mean_slice_s', n.get_float_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "resident_s": lambda n : setattr(self, 'resident_s', n.get_float_value()),
            "slices": lambda n : setattr(self, 'slices', n.get_int_value()),
            "swap_p50_s": lambda n : setattr(self, 'swap_p50_s', n.get_float_value()),
            "swap_p90_s": lambda n : setattr(self, 'swap_p90_s', n.get_float_value()),
            "swaps_measured": lambda n : setattr(self, 'swaps_measured', n.get_int_value()),
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
        writer.write_int_value("gpus", self.gpus)
        writer.write_str_value("logical_model", self.logical_model)
        writer.write_float_value("mean_slice_s", self.mean_slice_s)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_float_value("resident_s", self.resident_s)
        writer.write_int_value("slices", self.slices)
        writer.write_float_value("swap_p50_s", self.swap_p50_s)
        writer.write_float_value("swap_p90_s", self.swap_p90_s)
        writer.write_int_value("swaps_measured", self.swaps_measured)
        writer.write_additional_data_value(self.additional_data)
    

