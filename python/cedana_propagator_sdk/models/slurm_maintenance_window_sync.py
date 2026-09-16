from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SlurmMaintenanceWindowSync(AdditionalDataHolder, Parsable):
    """
    A SLURM maintenance reservation as reported by the cedana-slurm plugin
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The end_time property
    end_time: Optional[datetime.datetime] = None
    # The flags property
    flags: Optional[list[str]] = None
    # Reservation name, unique within the cluster
    name: Optional[str] = None
    # The nodes property
    nodes: Optional[list[str]] = None
    # The partitions property
    partitions: Optional[list[str]] = None
    # The reason property
    reason: Optional[str] = None
    # The start_time property
    start_time: Optional[datetime.datetime] = None
    # One of scheduled, active, completed, cancelled (defaults to scheduled)
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SlurmMaintenanceWindowSync:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SlurmMaintenanceWindowSync
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SlurmMaintenanceWindowSync()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "end_time": lambda n : setattr(self, 'end_time', n.get_datetime_value()),
            "flags": lambda n : setattr(self, 'flags', n.get_collection_of_primitive_values(str)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "nodes": lambda n : setattr(self, 'nodes', n.get_collection_of_primitive_values(str)),
            "partitions": lambda n : setattr(self, 'partitions', n.get_collection_of_primitive_values(str)),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "start_time": lambda n : setattr(self, 'start_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_datetime_value("end_time", self.end_time)
        writer.write_collection_of_primitive_values("flags", self.flags)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_primitive_values("nodes", self.nodes)
        writer.write_collection_of_primitive_values("partitions", self.partitions)
        writer.write_str_value("reason", self.reason)
        writer.write_datetime_value("start_time", self.start_time)
        writer.write_str_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

