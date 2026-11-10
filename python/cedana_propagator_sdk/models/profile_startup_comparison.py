from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .start_latency import StartLatency
    from .worker_start import WorkerStart

@dataclass
class ProfileStartupComparison(AdditionalDataHolder, Parsable):
    """
    Cold starts against restores, for one profile.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The cold property
    cold: Optional[StartLatency] = None
    # The logical_model property
    logical_model: Optional[str] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # The restored property
    restored: Optional[StartLatency] = None
    # Milliseconds a restore saves at the median.
    saved_ms: Optional[int] = None
    # Cold median divided by restore median. Above 1 means restoring is faster.
    speedup: Optional[float] = None
    # Every start behind the summaries, newest first.
    starts: Optional[list[WorkerStart]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProfileStartupComparison:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProfileStartupComparison
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProfileStartupComparison()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .start_latency import StartLatency
        from .worker_start import WorkerStart

        from .start_latency import StartLatency
        from .worker_start import WorkerStart

        fields: dict[str, Callable[[Any], None]] = {
            "cold": lambda n : setattr(self, 'cold', n.get_object_value(StartLatency)),
            "logical_model": lambda n : setattr(self, 'logical_model', n.get_str_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "restored": lambda n : setattr(self, 'restored', n.get_object_value(StartLatency)),
            "saved_ms": lambda n : setattr(self, 'saved_ms', n.get_int_value()),
            "speedup": lambda n : setattr(self, 'speedup', n.get_float_value()),
            "starts": lambda n : setattr(self, 'starts', n.get_collection_of_object_values(WorkerStart)),
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
        writer.write_object_value("cold", self.cold)
        writer.write_str_value("logical_model", self.logical_model)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_object_value("restored", self.restored)
        writer.write_int_value("saved_ms", self.saved_ms)
        writer.write_float_value("speedup", self.speedup)
        writer.write_collection_of_object_values("starts", self.starts)
        writer.write_additional_data_value(self.additional_data)
    

