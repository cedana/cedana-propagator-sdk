from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .failure_summary import FailureSummary
    from .histogram_bucket import HistogramBucket
    from .node_summary import NodeSummary
    from .operation_totals import OperationTotals
    from .stage_summary import StageSummary
    from .tier_summary import TierSummary
    from .timeline_point import TimelinePoint

@dataclass
class OperationsSummary(AdditionalDataHolder, Parsable):
    """
    Windowed aggregates over the same facts and bucket boundaries as the Prometheus export.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The artifact_size_buckets property
    artifact_size_buckets: Optional[list[HistogramBucket]] = None
    # The attempts property
    attempts: Optional[int] = None
    # The failed property
    failed: Optional[int] = None
    # The failures property
    failures: Optional[list[FailureSummary]] = None
    # The fallbacks property
    fallbacks: Optional[int] = None
    # Nodes that ran a checkpoint or restore in the window, busiest first.
    nodes: Optional[list[NodeSummary]] = None
    # The operations property
    operations: Optional[list[OperationTotals]] = None
    # The stages property
    stages: Optional[list[StageSummary]] = None
    # The step_seconds property
    step_seconds: Optional[int] = None
    # The succeeded property
    succeeded: Optional[int] = None
    # The tiers property
    tiers: Optional[list[TierSummary]] = None
    # The timeline property
    timeline: Optional[list[TimelinePoint]] = None
    # The window_seconds property
    window_seconds: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OperationsSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OperationsSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OperationsSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .failure_summary import FailureSummary
        from .histogram_bucket import HistogramBucket
        from .node_summary import NodeSummary
        from .operation_totals import OperationTotals
        from .stage_summary import StageSummary
        from .tier_summary import TierSummary
        from .timeline_point import TimelinePoint

        from .failure_summary import FailureSummary
        from .histogram_bucket import HistogramBucket
        from .node_summary import NodeSummary
        from .operation_totals import OperationTotals
        from .stage_summary import StageSummary
        from .tier_summary import TierSummary
        from .timeline_point import TimelinePoint

        fields: dict[str, Callable[[Any], None]] = {
            "artifact_size_buckets": lambda n : setattr(self, 'artifact_size_buckets', n.get_collection_of_object_values(HistogramBucket)),
            "attempts": lambda n : setattr(self, 'attempts', n.get_int_value()),
            "failed": lambda n : setattr(self, 'failed', n.get_int_value()),
            "failures": lambda n : setattr(self, 'failures', n.get_collection_of_object_values(FailureSummary)),
            "fallbacks": lambda n : setattr(self, 'fallbacks', n.get_int_value()),
            "nodes": lambda n : setattr(self, 'nodes', n.get_collection_of_object_values(NodeSummary)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(OperationTotals)),
            "stages": lambda n : setattr(self, 'stages', n.get_collection_of_object_values(StageSummary)),
            "step_seconds": lambda n : setattr(self, 'step_seconds', n.get_int_value()),
            "succeeded": lambda n : setattr(self, 'succeeded', n.get_int_value()),
            "tiers": lambda n : setattr(self, 'tiers', n.get_collection_of_object_values(TierSummary)),
            "timeline": lambda n : setattr(self, 'timeline', n.get_collection_of_object_values(TimelinePoint)),
            "window_seconds": lambda n : setattr(self, 'window_seconds', n.get_int_value()),
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
        writer.write_collection_of_object_values("artifact_size_buckets", self.artifact_size_buckets)
        writer.write_int_value("attempts", self.attempts)
        writer.write_int_value("failed", self.failed)
        writer.write_collection_of_object_values("failures", self.failures)
        writer.write_int_value("fallbacks", self.fallbacks)
        writer.write_collection_of_object_values("nodes", self.nodes)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("stages", self.stages)
        writer.write_int_value("step_seconds", self.step_seconds)
        writer.write_int_value("succeeded", self.succeeded)
        writer.write_collection_of_object_values("tiers", self.tiers)
        writer.write_collection_of_object_values("timeline", self.timeline)
        writer.write_int_value("window_seconds", self.window_seconds)
        writer.write_additional_data_value(self.additional_data)
    

