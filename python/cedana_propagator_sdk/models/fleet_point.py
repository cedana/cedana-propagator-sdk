from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class FleetPoint(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The gpus_in_use property
    gpus_in_use: Optional[float] = None
    # The gpus_total property
    gpus_total: Optional[float] = None
    # The ready_replicas property
    ready_replicas: Optional[float] = None
    # The serving_models property
    serving_models: Optional[int] = None
    # The ts property
    ts: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FleetPoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FleetPoint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FleetPoint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "gpus_in_use": lambda n : setattr(self, 'gpus_in_use', n.get_float_value()),
            "gpus_total": lambda n : setattr(self, 'gpus_total', n.get_float_value()),
            "ready_replicas": lambda n : setattr(self, 'ready_replicas', n.get_float_value()),
            "serving_models": lambda n : setattr(self, 'serving_models', n.get_int_value()),
            "ts": lambda n : setattr(self, 'ts', n.get_datetime_value()),
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
        writer.write_float_value("gpus_in_use", self.gpus_in_use)
        writer.write_float_value("gpus_total", self.gpus_total)
        writer.write_float_value("ready_replicas", self.ready_replicas)
        writer.write_int_value("serving_models", self.serving_models)
        writer.write_datetime_value("ts", self.ts)
        writer.write_additional_data_value(self.additional_data)
    

