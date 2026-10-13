from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class PodResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The age property
    age: Optional[str] = None
    # Cluster the pod runs on; null if the controller has not linked it yet
    cluster_id: Optional[UUID] = None
    # The id property
    id: Optional[UUID] = None
    # The monitored_by_policies property
    monitored_by_policies: Optional[list[str]] = None
    # The name property
    name: Optional[str] = None
    # The namespace property
    namespace: Optional[str] = None
    # The node property
    node: Optional[str] = None
    # The ready property
    ready: Optional[str] = None
    # The restarts property
    restarts: Optional[int] = None
    # The start_time property
    start_time: Optional[str] = None
    # The status property
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PodResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PodResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PodResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "age": lambda n : setattr(self, 'age', n.get_str_value()),
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_uuid_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "monitored_by_policies": lambda n : setattr(self, 'monitored_by_policies', n.get_collection_of_primitive_values(str)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "namespace": lambda n : setattr(self, 'namespace', n.get_str_value()),
            "node": lambda n : setattr(self, 'node', n.get_str_value()),
            "ready": lambda n : setattr(self, 'ready', n.get_str_value()),
            "restarts": lambda n : setattr(self, 'restarts', n.get_int_value()),
            "start_time": lambda n : setattr(self, 'start_time', n.get_str_value()),
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
        writer.write_str_value("age", self.age)
        writer.write_uuid_value("cluster_id", self.cluster_id)
        writer.write_uuid_value("id", self.id)
        writer.write_collection_of_primitive_values("monitored_by_policies", self.monitored_by_policies)
        writer.write_str_value("name", self.name)
        writer.write_str_value("namespace", self.namespace)
        writer.write_str_value("node", self.node)
        writer.write_str_value("ready", self.ready)
        writer.write_int_value("restarts", self.restarts)
        writer.write_str_value("start_time", self.start_time)
        writer.write_str_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

