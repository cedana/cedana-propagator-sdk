from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PolicyResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Cluster and namespace the policy targets, from `details`.
    cluster_id: Optional[str] = None
    # The end_time property
    end_time: Optional[datetime.datetime] = None
    # The id property
    id: Optional[str] = None
    # The input property
    input: Optional[int] = None
    # The job_count property
    job_count: Optional[int] = None
    # The namespace property
    namespace: Optional[str] = None
    # The pod_count property
    pod_count: Optional[int] = None
    # The policy_type property
    policy_type: Optional[str] = None
    # The resource property
    resource: Optional[str] = None
    # The resource_list property
    resource_list: Optional[list[str]] = None
    # Window bounds for maintenance policies; absent for other types.
    start_time: Optional[datetime.datetime] = None
    # The status property
    status: Optional[str] = None
    # The timestamp property
    timestamp: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PolicyResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_str_value()),
            "end_time": lambda n : setattr(self, 'end_time', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "input": lambda n : setattr(self, 'input', n.get_int_value()),
            "job_count": lambda n : setattr(self, 'job_count', n.get_int_value()),
            "namespace": lambda n : setattr(self, 'namespace', n.get_str_value()),
            "pod_count": lambda n : setattr(self, 'pod_count', n.get_int_value()),
            "policy_type": lambda n : setattr(self, 'policy_type', n.get_str_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_str_value()),
            "resource_list": lambda n : setattr(self, 'resource_list', n.get_collection_of_primitive_values(str)),
            "start_time": lambda n : setattr(self, 'start_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "timestamp": lambda n : setattr(self, 'timestamp', n.get_datetime_value()),
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
        writer.write_str_value("cluster_id", self.cluster_id)
        writer.write_datetime_value("end_time", self.end_time)
        writer.write_str_value("id", self.id)
        writer.write_int_value("input", self.input)
        writer.write_int_value("job_count", self.job_count)
        writer.write_str_value("namespace", self.namespace)
        writer.write_int_value("pod_count", self.pod_count)
        writer.write_str_value("policy_type", self.policy_type)
        writer.write_str_value("resource", self.resource)
        writer.write_collection_of_primitive_values("resource_list", self.resource_list)
        writer.write_datetime_value("start_time", self.start_time)
        writer.write_str_value("status", self.status)
        writer.write_datetime_value("timestamp", self.timestamp)
        writer.write_additional_data_value(self.additional_data)
    

