from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class SlurmJobSyncRequest(AdditionalDataHolder, Parsable):
    """
    Sync request containing a batch of jobs
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The cluster_id property
    cluster_id: Optional[UUID] = None
    # The batch is only some of the cluster's jobs: upsert them, but don'tmark the jobs missing from it as completed.
    partial: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SlurmJobSyncRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SlurmJobSyncRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SlurmJobSyncRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_uuid_value()),
            "partial": lambda n : setattr(self, 'partial', n.get_bool_value()),
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
        writer.write_uuid_value("cluster_id", self.cluster_id)
        writer.write_bool_value("partial", self.partial)
        writer.write_additional_data_value(self.additional_data)
    

