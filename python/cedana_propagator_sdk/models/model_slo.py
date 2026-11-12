from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .slo_thresholds import SloThresholds

@dataclass
class ModelSlo(AdditionalDataHolder, Parsable):
    """
    One model's service levels over the window, per serving profile.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Breached metrics: ttft_p95, error_rate, inter_token_p95. Empty below the minimum requests.
    breaches: Optional[list[str]] = None
    # The e2e_p95_ms property
    e2e_p95_ms: Optional[float] = None
    # The error_rate property
    error_rate: Optional[float] = None
    # 5xx and 429 responses; other 4xx are caller errors.
    errors: Optional[int] = None
    # p95 over requests of each request's p95 inter-token gap.
    inter_token_p95_ms: Optional[float] = None
    # The logical_model property
    logical_model: Optional[str] = None
    # The profile that served; null for requests refused before one was chosen.
    profile_id: Optional[str] = None
    # Time the gateway held the request before routing it.
    queue_p95_ms: Optional[float] = None
    # The requests property
    requests: Optional[int] = None
    # The thresholds property
    thresholds: Optional[SloThresholds] = None
    # The ttft_p50_ms property
    ttft_p50_ms: Optional[float] = None
    # Over every request, wakes included.
    ttft_p95_ms: Optional[float] = None
    # Requests that waited for the model to wake.
    wake_requests: Optional[int] = None
    # The wake_ttft_p95_ms property
    wake_ttft_p95_ms: Optional[float] = None
    # Requests routed within WAKE_QUEUE_MS; the TTFT breach is judged on these.
    warm_requests: Optional[int] = None
    # The warm_ttft_p95_ms property
    warm_ttft_p95_ms: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ModelSlo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ModelSlo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ModelSlo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .slo_thresholds import SloThresholds

        from .slo_thresholds import SloThresholds

        fields: dict[str, Callable[[Any], None]] = {
            "breaches": lambda n : setattr(self, 'breaches', n.get_collection_of_primitive_values(str)),
            "e2e_p95_ms": lambda n : setattr(self, 'e2e_p95_ms', n.get_float_value()),
            "error_rate": lambda n : setattr(self, 'error_rate', n.get_float_value()),
            "errors": lambda n : setattr(self, 'errors', n.get_int_value()),
            "inter_token_p95_ms": lambda n : setattr(self, 'inter_token_p95_ms', n.get_float_value()),
            "logical_model": lambda n : setattr(self, 'logical_model', n.get_str_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "queue_p95_ms": lambda n : setattr(self, 'queue_p95_ms', n.get_float_value()),
            "requests": lambda n : setattr(self, 'requests', n.get_int_value()),
            "thresholds": lambda n : setattr(self, 'thresholds', n.get_object_value(SloThresholds)),
            "ttft_p50_ms": lambda n : setattr(self, 'ttft_p50_ms', n.get_float_value()),
            "ttft_p95_ms": lambda n : setattr(self, 'ttft_p95_ms', n.get_float_value()),
            "wake_requests": lambda n : setattr(self, 'wake_requests', n.get_int_value()),
            "wake_ttft_p95_ms": lambda n : setattr(self, 'wake_ttft_p95_ms', n.get_float_value()),
            "warm_requests": lambda n : setattr(self, 'warm_requests', n.get_int_value()),
            "warm_ttft_p95_ms": lambda n : setattr(self, 'warm_ttft_p95_ms', n.get_float_value()),
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
        writer.write_collection_of_primitive_values("breaches", self.breaches)
        writer.write_float_value("e2e_p95_ms", self.e2e_p95_ms)
        writer.write_float_value("error_rate", self.error_rate)
        writer.write_int_value("errors", self.errors)
        writer.write_float_value("inter_token_p95_ms", self.inter_token_p95_ms)
        writer.write_str_value("logical_model", self.logical_model)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_float_value("queue_p95_ms", self.queue_p95_ms)
        writer.write_int_value("requests", self.requests)
        writer.write_object_value("thresholds", self.thresholds)
        writer.write_float_value("ttft_p50_ms", self.ttft_p50_ms)
        writer.write_float_value("ttft_p95_ms", self.ttft_p95_ms)
        writer.write_int_value("wake_requests", self.wake_requests)
        writer.write_float_value("wake_ttft_p95_ms", self.wake_ttft_p95_ms)
        writer.write_int_value("warm_requests", self.warm_requests)
        writer.write_float_value("warm_ttft_p95_ms", self.warm_ttft_p95_ms)
        writer.write_additional_data_value(self.additional_data)
    

