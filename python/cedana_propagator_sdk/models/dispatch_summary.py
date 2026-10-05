from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .dispatch_hold_outcomes import DispatchHoldOutcomes
    from .dispatch_hold_summary import DispatchHoldSummary
    from .dispatch_profile_summary import DispatchProfileSummary
    from .dispatch_series_point import DispatchSeriesPoint
    from .dispatch_totals import DispatchTotals
    from .dispatch_window import DispatchWindow
    from .dispatch_worker_summary import DispatchWorkerSummary

@dataclass
class DispatchSummary(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The by_profile property
    by_profile: Optional[list[DispatchProfileSummary]] = None
    # The by_worker property
    by_worker: Optional[list[DispatchWorkerSummary]] = None
    # What became of the requests that were parked: the restore-versus-coldpayoff, measured on the requests that waited for it.
    hold_outcomes: Optional[DispatchHoldOutcomes] = None
    # The holds property
    holds: Optional[list[DispatchHoldSummary]] = None
    # One point per minute over the window, by first-seen time.
    series: Optional[list[DispatchSeriesPoint]] = None
    # The totals property
    totals: Optional[DispatchTotals] = None
    # The window property
    window: Optional[DispatchWindow] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DispatchSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DispatchSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DispatchSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .dispatch_hold_outcomes import DispatchHoldOutcomes
        from .dispatch_hold_summary import DispatchHoldSummary
        from .dispatch_profile_summary import DispatchProfileSummary
        from .dispatch_series_point import DispatchSeriesPoint
        from .dispatch_totals import DispatchTotals
        from .dispatch_window import DispatchWindow
        from .dispatch_worker_summary import DispatchWorkerSummary

        from .dispatch_hold_outcomes import DispatchHoldOutcomes
        from .dispatch_hold_summary import DispatchHoldSummary
        from .dispatch_profile_summary import DispatchProfileSummary
        from .dispatch_series_point import DispatchSeriesPoint
        from .dispatch_totals import DispatchTotals
        from .dispatch_window import DispatchWindow
        from .dispatch_worker_summary import DispatchWorkerSummary

        fields: dict[str, Callable[[Any], None]] = {
            "by_profile": lambda n : setattr(self, 'by_profile', n.get_collection_of_object_values(DispatchProfileSummary)),
            "by_worker": lambda n : setattr(self, 'by_worker', n.get_collection_of_object_values(DispatchWorkerSummary)),
            "hold_outcomes": lambda n : setattr(self, 'hold_outcomes', n.get_object_value(DispatchHoldOutcomes)),
            "holds": lambda n : setattr(self, 'holds', n.get_collection_of_object_values(DispatchHoldSummary)),
            "series": lambda n : setattr(self, 'series', n.get_collection_of_object_values(DispatchSeriesPoint)),
            "totals": lambda n : setattr(self, 'totals', n.get_object_value(DispatchTotals)),
            "window": lambda n : setattr(self, 'window', n.get_object_value(DispatchWindow)),
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
        writer.write_collection_of_object_values("by_profile", self.by_profile)
        writer.write_collection_of_object_values("by_worker", self.by_worker)
        writer.write_object_value("hold_outcomes", self.hold_outcomes)
        writer.write_collection_of_object_values("holds", self.holds)
        writer.write_collection_of_object_values("series", self.series)
        writer.write_object_value("totals", self.totals)
        writer.write_object_value("window", self.window)
        writer.write_additional_data_value(self.additional_data)
    

