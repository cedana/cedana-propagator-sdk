from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class Cluster(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The connector property
    connector: Optional[str] = None
    # The id property
    id: Optional[UUID] = None
    # The k8s_version property
    k8s_version: Optional[str] = None
    # The kind property
    kind: Optional[str] = None
    # The last_sync property
    last_sync: Optional[datetime.datetime] = None
    # The name property
    name: Optional[str] = None
    # The status property
    status: Optional[str] = None
    # The sync_mode property
    sync_mode: Optional[str] = None
    # The watch_reason property
    watch_reason: Optional[str] = None
    # The watch_state property
    watch_state: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Cluster:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Cluster
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Cluster()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "connector": lambda n : setattr(self, 'connector', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "k8s_version": lambda n : setattr(self, 'k8s_version', n.get_str_value()),
            "kind": lambda n : setattr(self, 'kind', n.get_str_value()),
            "last_sync": lambda n : setattr(self, 'last_sync', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "sync_mode": lambda n : setattr(self, 'sync_mode', n.get_str_value()),
            "watch_reason": lambda n : setattr(self, 'watch_reason', n.get_str_value()),
            "watch_state": lambda n : setattr(self, 'watch_state', n.get_str_value()),
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
        writer.write_str_value("connector", self.connector)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("k8s_version", self.k8s_version)
        writer.write_str_value("kind", self.kind)
        writer.write_datetime_value("last_sync", self.last_sync)
        writer.write_str_value("name", self.name)
        writer.write_str_value("status", self.status)
        writer.write_str_value("sync_mode", self.sync_mode)
        writer.write_str_value("watch_reason", self.watch_reason)
        writer.write_str_value("watch_state", self.watch_state)
        writer.write_additional_data_value(self.additional_data)
    

