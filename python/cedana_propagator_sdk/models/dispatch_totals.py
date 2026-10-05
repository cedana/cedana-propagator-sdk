from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DispatchTotals(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The assigned property
    assigned: Optional[int] = None
    # The fallback property
    fallback: Optional[int] = None
    # The kv_affinity property
    kv_affinity: Optional[int] = None
    # The parked property
    parked: Optional[int] = None
    # The rejected property
    rejected: Optional[int] = None
    # The served_by_cold_worker property
    served_by_cold_worker: Optional[int] = None
    # The served_by_restored_worker property
    served_by_restored_worker: Optional[int] = None
    # The served_unattributed property
    served_unattributed: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DispatchTotals:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DispatchTotals
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DispatchTotals()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "assigned": lambda n : setattr(self, 'assigned', n.get_int_value()),
            "fallback": lambda n : setattr(self, 'fallback', n.get_int_value()),
            "kv_affinity": lambda n : setattr(self, 'kv_affinity', n.get_int_value()),
            "parked": lambda n : setattr(self, 'parked', n.get_int_value()),
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
        writer.write_int_value("fallback", self.fallback)
        writer.write_int_value("kv_affinity", self.kv_affinity)
        writer.write_int_value("parked", self.parked)
        writer.write_int_value("rejected", self.rejected)
        writer.write_int_value("served_by_cold_worker", self.served_by_cold_worker)
        writer.write_int_value("served_by_restored_worker", self.served_by_restored_worker)
        writer.write_int_value("served_unattributed", self.served_unattributed)
        writer.write_additional_data_value(self.additional_data)
    

