from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class JobResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The age property
    age: Optional[str] = None
    # The cluster_id property
    cluster_id: Optional[UUID] = None
    # The completions property
    completions: Optional[str] = None
    # The created_at property
    created_at: Optional[datetime.datetime] = None
    # The duration property
    duration: Optional[str] = None
    # The id property
    id: Optional[UUID] = None
    # The monitored_by_policies property
    monitored_by_policies: Optional[list[str]] = None
    # The name property
    name: Optional[str] = None
    # The namespace property
    namespace: Optional[str] = None
    # The pod_count property
    pod_count: Optional[int] = None
    # The pod_ids property
    pod_ids: Optional[list[str]] = None
    # The policy_count property
    policy_count: Optional[int] = None
    # The priority property
    priority: Optional[int] = None
    # The resource_version property
    resource_version: Optional[str] = None
    # The startTime property
    start_time: Optional[str] = None
    # The status property
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "age": lambda n : setattr(self, 'age', n.get_str_value()),
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_uuid_value()),
            "completions": lambda n : setattr(self, 'completions', n.get_str_value()),
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "monitored_by_policies": lambda n : setattr(self, 'monitored_by_policies', n.get_collection_of_primitive_values(str)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "namespace": lambda n : setattr(self, 'namespace', n.get_str_value()),
            "pod_count": lambda n : setattr(self, 'pod_count', n.get_int_value()),
            "pod_ids": lambda n : setattr(self, 'pod_ids', n.get_collection_of_primitive_values(str)),
            "policy_count": lambda n : setattr(self, 'policy_count', n.get_int_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "resource_version": lambda n : setattr(self, 'resource_version', n.get_str_value()),
            "startTime": lambda n : setattr(self, 'start_time', n.get_str_value()),
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
        writer.write_str_value("completions", self.completions)
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_str_value("duration", self.duration)
        writer.write_uuid_value("id", self.id)
        writer.write_collection_of_primitive_values("monitored_by_policies", self.monitored_by_policies)
        writer.write_str_value("name", self.name)
        writer.write_str_value("namespace", self.namespace)
        writer.write_int_value("pod_count", self.pod_count)
        writer.write_collection_of_primitive_values("pod_ids", self.pod_ids)
        writer.write_int_value("policy_count", self.policy_count)
        writer.write_int_value("priority", self.priority)
        writer.write_str_value("resource_version", self.resource_version)
        writer.write_str_value("startTime", self.start_time)
        writer.write_str_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

