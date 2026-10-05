from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DispatchView(AdditionalDataHolder, Parsable):
    """
    One dispatch, joined with the completion facts once Switchyard hasreported them. `completed` false means the request is still in flight orits telemetry never arrived; every usage field is then null.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The activation_path property
    activation_path: Optional[str] = None
    # The active_streams property
    active_streams: Optional[int] = None
    # The attempts property
    attempts: Optional[int] = None
    # The cached_tokens property
    cached_tokens: Optional[int] = None
    # The completed property
    completed: Optional[bool] = None
    # The completion_tokens property
    completion_tokens: Optional[int] = None
    # The created_at property
    created_at: Optional[datetime.datetime] = None
    # The decision_source property
    decision_source: Optional[str] = None
    # The dispatch_id property
    dispatch_id: Optional[int] = None
    # The end_to_end_latency_ms property
    end_to_end_latency_ms: Optional[int] = None
    # The estimated_prompt_tokens property
    estimated_prompt_tokens: Optional[int] = None
    # The expected_ready_ms property
    expected_ready_ms: Optional[int] = None
    # The expected_reuse_tokens property
    expected_reuse_tokens: Optional[int] = None
    # The fallback_used property
    fallback_used: Optional[bool] = None
    # The path a held request was forecast on: restore or cold. Distinctfrom the usage row's `activation_path`, which is what actually served.
    forecast_path: Optional[str] = None
    # The hold_budget_ms property
    hold_budget_ms: Optional[int] = None
    # The hold_reason property
    hold_reason: Optional[str] = None
    # The logical_model property
    logical_model: Optional[str] = None
    # The outcome property
    outcome: Optional[str] = None
    # The preference_reason property
    preference_reason: Optional[str] = None
    # The preferred_profile_id property
    preferred_profile_id: Optional[str] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # The prompt_tokens property
    prompt_tokens: Optional[int] = None
    # The queued_requests property
    queued_requests: Optional[int] = None
    # The ready_replicas property
    ready_replicas: Optional[int] = None
    # The request_id property
    request_id: Optional[str] = None
    # The retry_after_ms property
    retry_after_ms: Optional[int] = None
    # The status_code property
    status_code: Optional[int] = None
    # The ttft_ms property
    ttft_ms: Optional[int] = None
    # The updated_at property
    updated_at: Optional[datetime.datetime] = None
    # `pod` or `profile`: how far the worker columns can be trusted.
    worker_basis: Optional[str] = None
    # The worker_checkpoint_path property
    worker_checkpoint_path: Optional[str] = None
    # The worker_node_name property
    worker_node_name: Optional[str] = None
    # The worker_pod_name property
    worker_pod_name: Optional[str] = None
    # The worker_start_kind property
    worker_start_kind: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DispatchView:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DispatchView
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DispatchView()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "activation_path": lambda n : setattr(self, 'activation_path', n.get_str_value()),
            "active_streams": lambda n : setattr(self, 'active_streams', n.get_int_value()),
            "attempts": lambda n : setattr(self, 'attempts', n.get_int_value()),
            "cached_tokens": lambda n : setattr(self, 'cached_tokens', n.get_int_value()),
            "completed": lambda n : setattr(self, 'completed', n.get_bool_value()),
            "completion_tokens": lambda n : setattr(self, 'completion_tokens', n.get_int_value()),
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "decision_source": lambda n : setattr(self, 'decision_source', n.get_str_value()),
            "dispatch_id": lambda n : setattr(self, 'dispatch_id', n.get_int_value()),
            "end_to_end_latency_ms": lambda n : setattr(self, 'end_to_end_latency_ms', n.get_int_value()),
            "estimated_prompt_tokens": lambda n : setattr(self, 'estimated_prompt_tokens', n.get_int_value()),
            "expected_ready_ms": lambda n : setattr(self, 'expected_ready_ms', n.get_int_value()),
            "expected_reuse_tokens": lambda n : setattr(self, 'expected_reuse_tokens', n.get_int_value()),
            "fallback_used": lambda n : setattr(self, 'fallback_used', n.get_bool_value()),
            "forecast_path": lambda n : setattr(self, 'forecast_path', n.get_str_value()),
            "hold_budget_ms": lambda n : setattr(self, 'hold_budget_ms', n.get_int_value()),
            "hold_reason": lambda n : setattr(self, 'hold_reason', n.get_str_value()),
            "logical_model": lambda n : setattr(self, 'logical_model', n.get_str_value()),
            "outcome": lambda n : setattr(self, 'outcome', n.get_str_value()),
            "preference_reason": lambda n : setattr(self, 'preference_reason', n.get_str_value()),
            "preferred_profile_id": lambda n : setattr(self, 'preferred_profile_id', n.get_str_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "prompt_tokens": lambda n : setattr(self, 'prompt_tokens', n.get_int_value()),
            "queued_requests": lambda n : setattr(self, 'queued_requests', n.get_int_value()),
            "ready_replicas": lambda n : setattr(self, 'ready_replicas', n.get_int_value()),
            "request_id": lambda n : setattr(self, 'request_id', n.get_str_value()),
            "retry_after_ms": lambda n : setattr(self, 'retry_after_ms', n.get_int_value()),
            "status_code": lambda n : setattr(self, 'status_code', n.get_int_value()),
            "ttft_ms": lambda n : setattr(self, 'ttft_ms', n.get_int_value()),
            "updated_at": lambda n : setattr(self, 'updated_at', n.get_datetime_value()),
            "worker_basis": lambda n : setattr(self, 'worker_basis', n.get_str_value()),
            "worker_checkpoint_path": lambda n : setattr(self, 'worker_checkpoint_path', n.get_str_value()),
            "worker_node_name": lambda n : setattr(self, 'worker_node_name', n.get_str_value()),
            "worker_pod_name": lambda n : setattr(self, 'worker_pod_name', n.get_str_value()),
            "worker_start_kind": lambda n : setattr(self, 'worker_start_kind', n.get_str_value()),
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
        writer.write_int_value("active_streams", self.active_streams)
        writer.write_int_value("attempts", self.attempts)
        writer.write_int_value("cached_tokens", self.cached_tokens)
        writer.write_bool_value("completed", self.completed)
        writer.write_int_value("completion_tokens", self.completion_tokens)
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_str_value("decision_source", self.decision_source)
        writer.write_int_value("dispatch_id", self.dispatch_id)
        writer.write_int_value("end_to_end_latency_ms", self.end_to_end_latency_ms)
        writer.write_int_value("estimated_prompt_tokens", self.estimated_prompt_tokens)
        writer.write_int_value("expected_ready_ms", self.expected_ready_ms)
        writer.write_int_value("expected_reuse_tokens", self.expected_reuse_tokens)
        writer.write_bool_value("fallback_used", self.fallback_used)
        writer.write_str_value("forecast_path", self.forecast_path)
        writer.write_int_value("hold_budget_ms", self.hold_budget_ms)
        writer.write_str_value("hold_reason", self.hold_reason)
        writer.write_str_value("logical_model", self.logical_model)
        writer.write_str_value("outcome", self.outcome)
        writer.write_str_value("preference_reason", self.preference_reason)
        writer.write_str_value("preferred_profile_id", self.preferred_profile_id)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_int_value("prompt_tokens", self.prompt_tokens)
        writer.write_int_value("queued_requests", self.queued_requests)
        writer.write_int_value("ready_replicas", self.ready_replicas)
        writer.write_str_value("request_id", self.request_id)
        writer.write_int_value("retry_after_ms", self.retry_after_ms)
        writer.write_int_value("status_code", self.status_code)
        writer.write_int_value("ttft_ms", self.ttft_ms)
        writer.write_datetime_value("updated_at", self.updated_at)
        writer.write_str_value("worker_basis", self.worker_basis)
        writer.write_str_value("worker_checkpoint_path", self.worker_checkpoint_path)
        writer.write_str_value("worker_node_name", self.worker_node_name)
        writer.write_str_value("worker_pod_name", self.worker_pod_name)
        writer.write_str_value("worker_start_kind", self.worker_start_kind)
        writer.write_additional_data_value(self.additional_data)
    

