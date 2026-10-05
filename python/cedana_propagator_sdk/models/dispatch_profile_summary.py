from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DispatchProfileSummary(AdditionalDataHolder, Parsable):
    """
    Per profile: how requests were dispatched to it and what served them.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The assigned property
    assigned: Optional[int] = None
    # The avg_ttft_ms property
    avg_ttft_ms: Optional[float] = None
    # Engine-reported cached prompt tokens, summed. Null when nothingreported it, never zero.
    cached_tokens: Optional[int] = None
    # The classifier property
    classifier: Optional[int] = None
    # The completed property
    completed: Optional[int] = None
    # The completion_tokens property
    completion_tokens: Optional[int] = None
    # The expected_reuse_tokens property
    expected_reuse_tokens: Optional[int] = None
    # The failed property
    failed: Optional[int] = None
    # The fallback property
    fallback: Optional[int] = None
    # Assigned because Switchyard's prefix affinity asked for this profile.
    kv_affinity: Optional[int] = None
    # The logical_model property
    logical_model: Optional[str] = None
    # The p50_ttft_ms property
    p50_ttft_ms: Optional[float] = None
    # The parked property
    parked: Optional[int] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # The prompt_tokens property
    prompt_tokens: Optional[int] = None
    # The rejected property
    rejected: Optional[int] = None
    # The served_by_cold_worker property
    served_by_cold_worker: Optional[int] = None
    # Assigned to a worker that had restored from a checkpoint.
    served_by_restored_worker: Optional[int] = None
    # Assigned with no single worker to attribute (several replicas, or nopod visible). Counted separately so the two above never look completewhen they are not.
    served_unattributed: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DispatchProfileSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DispatchProfileSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DispatchProfileSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "assigned": lambda n : setattr(self, 'assigned', n.get_int_value()),
            "avg_ttft_ms": lambda n : setattr(self, 'avg_ttft_ms', n.get_float_value()),
            "cached_tokens": lambda n : setattr(self, 'cached_tokens', n.get_int_value()),
            "classifier": lambda n : setattr(self, 'classifier', n.get_int_value()),
            "completed": lambda n : setattr(self, 'completed', n.get_int_value()),
            "completion_tokens": lambda n : setattr(self, 'completion_tokens', n.get_int_value()),
            "expected_reuse_tokens": lambda n : setattr(self, 'expected_reuse_tokens', n.get_int_value()),
            "failed": lambda n : setattr(self, 'failed', n.get_int_value()),
            "fallback": lambda n : setattr(self, 'fallback', n.get_int_value()),
            "kv_affinity": lambda n : setattr(self, 'kv_affinity', n.get_int_value()),
            "logical_model": lambda n : setattr(self, 'logical_model', n.get_str_value()),
            "p50_ttft_ms": lambda n : setattr(self, 'p50_ttft_ms', n.get_float_value()),
            "parked": lambda n : setattr(self, 'parked', n.get_int_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "prompt_tokens": lambda n : setattr(self, 'prompt_tokens', n.get_int_value()),
            "rejected": lambda n : setattr(self, 'rejected', n.get_int_value()),
            "served_by_cold_worker": lambda n : setattr(self, 'served_by_cold_worker', n.get_int_value()),
            "served_by_restored_worker": lambda n : setattr(self, 'served_by_restored_worker', n.get_int_value()),
            "served_unattributed": lambda n : setattr(self, 'served_unattributed', n.get_int_value()),
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
        writer.write_int_value("assigned", self.assigned)
        writer.write_float_value("avg_ttft_ms", self.avg_ttft_ms)
        writer.write_int_value("cached_tokens", self.cached_tokens)
        writer.write_int_value("classifier", self.classifier)
        writer.write_int_value("completed", self.completed)
        writer.write_int_value("completion_tokens", self.completion_tokens)
        writer.write_int_value("expected_reuse_tokens", self.expected_reuse_tokens)
        writer.write_int_value("failed", self.failed)
        writer.write_int_value("fallback", self.fallback)
        writer.write_int_value("kv_affinity", self.kv_affinity)
        writer.write_str_value("logical_model", self.logical_model)
        writer.write_float_value("p50_ttft_ms", self.p50_ttft_ms)
        writer.write_int_value("parked", self.parked)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_int_value("prompt_tokens", self.prompt_tokens)
        writer.write_int_value("rejected", self.rejected)
        writer.write_int_value("served_by_cold_worker", self.served_by_cold_worker)
        writer.write_int_value("served_by_restored_worker", self.served_by_restored_worker)
        writer.write_int_value("served_unattributed", self.served_unattributed)
        writer.write_additional_data_value(self.additional_data)
    

