from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TelemetryRecord(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The activation_path property
    activation_path: Optional[str] = None
    # The classifier_latency_ms property
    classifier_latency_ms: Optional[int] = None
    # The classifier_profile_id property
    classifier_profile_id: Optional[str] = None
    # The completed_at_ms property
    completed_at_ms: Optional[int] = None
    # The completion_tokens property
    completion_tokens: Optional[int] = None
    # The decision_source property
    decision_source: Optional[str] = None
    # The end_to_end_latency_ms property
    end_to_end_latency_ms: Optional[int] = None
    # The fallback_used property
    fallback_used: Optional[bool] = None
    # The logical_model property
    logical_model: Optional[str] = None
    # The mean_inter_token_ms property
    mean_inter_token_ms: Optional[float] = None
    # The p95_inter_token_ms property
    p95_inter_token_ms: Optional[float] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # The prompt_tokens property
    prompt_tokens: Optional[int] = None
    # The queue_ms property
    queue_ms: Optional[int] = None
    # The request_id property
    request_id: Optional[str] = None
    # The route_generation property
    route_generation: Optional[int] = None
    # The started_at_ms property
    started_at_ms: Optional[int] = None
    # The status_code property
    status_code: Optional[int] = None
    # The stream_duration_ms property
    stream_duration_ms: Optional[int] = None
    # The ttft_ms property
    ttft_ms: Optional[int] = None
    # The upstream_attempts property
    upstream_attempts: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TelemetryRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TelemetryRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TelemetryRecord()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "activation_path": lambda n : setattr(self, 'activation_path', n.get_str_value()),
            "classifier_latency_ms": lambda n : setattr(self, 'classifier_latency_ms', n.get_int_value()),
            "classifier_profile_id": lambda n : setattr(self, 'classifier_profile_id', n.get_str_value()),
            "completed_at_ms": lambda n : setattr(self, 'completed_at_ms', n.get_int_value()),
            "completion_tokens": lambda n : setattr(self, 'completion_tokens', n.get_int_value()),
            "decision_source": lambda n : setattr(self, 'decision_source', n.get_str_value()),
            "end_to_end_latency_ms": lambda n : setattr(self, 'end_to_end_latency_ms', n.get_int_value()),
            "fallback_used": lambda n : setattr(self, 'fallback_used', n.get_bool_value()),
            "logical_model": lambda n : setattr(self, 'logical_model', n.get_str_value()),
            "mean_inter_token_ms": lambda n : setattr(self, 'mean_inter_token_ms', n.get_float_value()),
            "p95_inter_token_ms": lambda n : setattr(self, 'p95_inter_token_ms', n.get_float_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "prompt_tokens": lambda n : setattr(self, 'prompt_tokens', n.get_int_value()),
            "queue_ms": lambda n : setattr(self, 'queue_ms', n.get_int_value()),
            "request_id": lambda n : setattr(self, 'request_id', n.get_str_value()),
            "route_generation": lambda n : setattr(self, 'route_generation', n.get_int_value()),
            "started_at_ms": lambda n : setattr(self, 'started_at_ms', n.get_int_value()),
            "status_code": lambda n : setattr(self, 'status_code', n.get_int_value()),
            "stream_duration_ms": lambda n : setattr(self, 'stream_duration_ms', n.get_int_value()),
            "ttft_ms": lambda n : setattr(self, 'ttft_ms', n.get_int_value()),
            "upstream_attempts": lambda n : setattr(self, 'upstream_attempts', n.get_int_value()),
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
        writer.write_int_value("classifier_latency_ms", self.classifier_latency_ms)
        writer.write_str_value("classifier_profile_id", self.classifier_profile_id)
        writer.write_int_value("completed_at_ms", self.completed_at_ms)
        writer.write_int_value("completion_tokens", self.completion_tokens)
        writer.write_str_value("decision_source", self.decision_source)
        writer.write_int_value("end_to_end_latency_ms", self.end_to_end_latency_ms)
        writer.write_bool_value("fallback_used", self.fallback_used)
        writer.write_str_value("logical_model", self.logical_model)
        writer.write_float_value("mean_inter_token_ms", self.mean_inter_token_ms)
        writer.write_float_value("p95_inter_token_ms", self.p95_inter_token_ms)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_int_value("prompt_tokens", self.prompt_tokens)
        writer.write_int_value("queue_ms", self.queue_ms)
        writer.write_str_value("request_id", self.request_id)
        writer.write_int_value("route_generation", self.route_generation)
        writer.write_int_value("started_at_ms", self.started_at_ms)
        writer.write_int_value("status_code", self.status_code)
        writer.write_int_value("stream_duration_ms", self.stream_duration_ms)
        writer.write_int_value("ttft_ms", self.ttft_ms)
        writer.write_int_value("upstream_attempts", self.upstream_attempts)
        writer.write_additional_data_value(self.additional_data)
    

