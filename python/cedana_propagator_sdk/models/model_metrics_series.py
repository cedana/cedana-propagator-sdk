from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .model_metrics_series_points import ModelMetricsSeries_points

@dataclass
class ModelMetricsSeries(AdditionalDataHolder, Parsable):
    """
    A model's engine and GPU metrics in one bucket: `ts` plus one field per recorded series(generation_tokens_per_second, kv_usage, gpu_utilization, ...); a series with no samples is absent.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The points property
    points: Optional[list[ModelMetricsSeries_points]] = None
    # The profile_id property
    profile_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ModelMetricsSeries:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ModelMetricsSeries
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ModelMetricsSeries()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .model_metrics_series_points import ModelMetricsSeries_points

        from .model_metrics_series_points import ModelMetricsSeries_points

        fields: dict[str, Callable[[Any], None]] = {
            "points": lambda n : setattr(self, 'points', n.get_collection_of_object_values(ModelMetricsSeries_points)),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
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
        writer.write_collection_of_object_values("points", self.points)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_additional_data_value(self.additional_data)
    

