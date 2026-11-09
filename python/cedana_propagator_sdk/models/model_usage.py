from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ModelUsage(AdditionalDataHolder, Parsable):
    """
    Served traffic for one model over the window, from the gateway's per-request records.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The completion_tokens property
    completion_tokens: Optional[int] = None
    # The errors property
    errors: Optional[int] = None
    # The logical_model property
    logical_model: Optional[str] = None
    # Completion tokens over streaming time, per request stream.
    output_tokens_per_second: Optional[float] = None
    # The prompt_tokens property
    prompt_tokens: Optional[int] = None
    # The requests property
    requests: Optional[int] = None
    # The ttft_p50_ms property
    ttft_p50_ms: Optional[float] = None
    # The ttft_p95_ms property
    ttft_p95_ms: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ModelUsage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ModelUsage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ModelUsage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "completion_tokens": lambda n : setattr(self, 'completion_tokens', n.get_int_value()),
            "errors": lambda n : setattr(self, 'errors', n.get_int_value()),
            "logical_model": lambda n : setattr(self, 'logical_model', n.get_str_value()),
            "output_tokens_per_second": lambda n : setattr(self, 'output_tokens_per_second', n.get_float_value()),
            "prompt_tokens": lambda n : setattr(self, 'prompt_tokens', n.get_int_value()),
            "requests": lambda n : setattr(self, 'requests', n.get_int_value()),
            "ttft_p50_ms": lambda n : setattr(self, 'ttft_p50_ms', n.get_float_value()),
            "ttft_p95_ms": lambda n : setattr(self, 'ttft_p95_ms', n.get_float_value()),
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
        writer.write_int_value("completion_tokens", self.completion_tokens)
        writer.write_int_value("errors", self.errors)
        writer.write_str_value("logical_model", self.logical_model)
        writer.write_float_value("output_tokens_per_second", self.output_tokens_per_second)
        writer.write_int_value("prompt_tokens", self.prompt_tokens)
        writer.write_int_value("requests", self.requests)
        writer.write_float_value("ttft_p50_ms", self.ttft_p50_ms)
        writer.write_float_value("ttft_p95_ms", self.ttft_p95_ms)
        writer.write_additional_data_value(self.additional_data)
    

