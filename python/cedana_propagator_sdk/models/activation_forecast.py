from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ActivationForecast(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # `measured` from this profile's own workers on this path, `estimated`from the profile's registered cold-start estimate, or `unknown`.
    basis: Optional[str] = None
    # How long the pending worker has been starting, when one is visible.
    elapsed_ms: Optional[int] = None
    # Median and p95 time still to go, never negative. Null when nothing isknown; a router must then fall back to its default poll.
    expected_remaining_ms: Optional[int] = None
    # Median start-to-ready on this path, from scheduling to Ready.
    expected_total_ms: Optional[int] = None
    # The p95_remaining_ms property
    p95_remaining_ms: Optional[int] = None
    # The p95_total_ms property
    p95_total_ms: Optional[int] = None
    # `restore` or `cold`: the path the pending worker is (or will be) on.
    path: Optional[str] = None
    # How the path was decided: `pod` (the pending pod carries a checkpointpath, or does not), `artifact` (no pod yet, but a ready checkpointexists for this profile's compatibility key), or `none` (no pod, noartifact — a cold start is the only thing that can happen).
    path_basis: Optional[str] = None
    # The samples property
    samples: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ActivationForecast:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ActivationForecast
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ActivationForecast()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "basis": lambda n : setattr(self, 'basis', n.get_str_value()),
            "elapsed_ms": lambda n : setattr(self, 'elapsed_ms', n.get_int_value()),
            "expected_remaining_ms": lambda n : setattr(self, 'expected_remaining_ms', n.get_int_value()),
            "expected_total_ms": lambda n : setattr(self, 'expected_total_ms', n.get_int_value()),
            "p95_remaining_ms": lambda n : setattr(self, 'p95_remaining_ms', n.get_int_value()),
            "p95_total_ms": lambda n : setattr(self, 'p95_total_ms', n.get_int_value()),
            "path": lambda n : setattr(self, 'path', n.get_str_value()),
            "path_basis": lambda n : setattr(self, 'path_basis', n.get_str_value()),
            "samples": lambda n : setattr(self, 'samples', n.get_int_value()),
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
        writer.write_str_value("basis", self.basis)
        writer.write_int_value("elapsed_ms", self.elapsed_ms)
        writer.write_int_value("expected_remaining_ms", self.expected_remaining_ms)
        writer.write_int_value("expected_total_ms", self.expected_total_ms)
        writer.write_int_value("p95_remaining_ms", self.p95_remaining_ms)
        writer.write_int_value("p95_total_ms", self.p95_total_ms)
        writer.write_str_value("path", self.path)
        writer.write_str_value("path_basis", self.path_basis)
        writer.write_int_value("samples", self.samples)
        writer.write_additional_data_value(self.additional_data)
    

