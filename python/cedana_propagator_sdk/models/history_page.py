from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .history_cursor import HistoryCursor
    from .history_record import HistoryRecord

@dataclass
class HistoryPage(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The next property
    next: Optional[HistoryCursor] = None
    # The records property
    records: Optional[list[HistoryRecord]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HistoryPage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HistoryPage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HistoryPage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .history_cursor import HistoryCursor
        from .history_record import HistoryRecord

        from .history_cursor import HistoryCursor
        from .history_record import HistoryRecord

        fields: dict[str, Callable[[Any], None]] = {
            "next": lambda n : setattr(self, 'next', n.get_object_value(HistoryCursor)),
            "records": lambda n : setattr(self, 'records', n.get_collection_of_object_values(HistoryRecord)),
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
        writer.write_object_value("next", self.next)
        writer.write_collection_of_object_values("records", self.records)
        writer.write_additional_data_value(self.additional_data)
    

