from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class NotificationEvent(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Storage rows: the CSX action (cached, evicted, persisted, read_closed, ...); empty otherwise.
    action: Optional[str] = None
    # The action_id property
    action_id: Optional[str] = None
    # The checkpoint_id property
    checkpoint_id: Optional[str] = None
    # The cluster_id property
    cluster_id: Optional[str] = None
    # The context property
    context: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The duration_ns property
    duration_ns: Optional[int] = None
    # The failure_reason property
    failure_reason: Optional[str] = None
    # The failure_stage property
    failure_stage: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The namespace property
    namespace: Optional[str] = None
    # The node_name property
    node_name: Optional[str] = None
    # The operation property
    operation: Optional[str] = None
    # Checkpoints: time the workload was held (see facts::checkpoint_pause_ns).
    pause_ns: Optional[int] = None
    # The physical_bytes property
    physical_bytes: Optional[int] = None
    # The pod_ready_at_ms property
    pod_ready_at_ms: Optional[int] = None
    # Restores: PodScheduled / Ready transitions of the restored pod, once known.
    pod_scheduled_at_ms: Optional[int] = None
    # The pod_uid property
    pod_uid: Optional[str] = None
    # The read property
    read: Optional[bool] = None
    # The restore_uuid property
    restore_uuid: Optional[str] = None
    # The result property
    result: Optional[str] = None
    # The storage_tier property
    storage_tier: Optional[str] = None
    # The timestamp property
    timestamp: Optional[str] = None
    # The type property
    type: Optional[str] = None
    # The workload_type property
    workload_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NotificationEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NotificationEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NotificationEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_str_value()),
            "action_id": lambda n : setattr(self, 'action_id', n.get_str_value()),
            "checkpoint_id": lambda n : setattr(self, 'checkpoint_id', n.get_str_value()),
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_str_value()),
            "context": lambda n : setattr(self, 'context', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "duration_ns": lambda n : setattr(self, 'duration_ns', n.get_int_value()),
            "failure_reason": lambda n : setattr(self, 'failure_reason', n.get_str_value()),
            "failure_stage": lambda n : setattr(self, 'failure_stage', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "namespace": lambda n : setattr(self, 'namespace', n.get_str_value()),
            "node_name": lambda n : setattr(self, 'node_name', n.get_str_value()),
            "operation": lambda n : setattr(self, 'operation', n.get_str_value()),
            "pause_ns": lambda n : setattr(self, 'pause_ns', n.get_int_value()),
            "physical_bytes": lambda n : setattr(self, 'physical_bytes', n.get_int_value()),
            "pod_ready_at_ms": lambda n : setattr(self, 'pod_ready_at_ms', n.get_int_value()),
            "pod_scheduled_at_ms": lambda n : setattr(self, 'pod_scheduled_at_ms', n.get_int_value()),
            "pod_uid": lambda n : setattr(self, 'pod_uid', n.get_str_value()),
            "read": lambda n : setattr(self, 'read', n.get_bool_value()),
            "restore_uuid": lambda n : setattr(self, 'restore_uuid', n.get_str_value()),
            "result": lambda n : setattr(self, 'result', n.get_str_value()),
            "storage_tier": lambda n : setattr(self, 'storage_tier', n.get_str_value()),
            "timestamp": lambda n : setattr(self, 'timestamp', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "workload_type": lambda n : setattr(self, 'workload_type', n.get_str_value()),
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
        writer.write_str_value("action", self.action)
        writer.write_str_value("action_id", self.action_id)
        writer.write_str_value("checkpoint_id", self.checkpoint_id)
        writer.write_str_value("cluster_id", self.cluster_id)
        writer.write_str_value("context", self.context)
        writer.write_str_value("description", self.description)
        writer.write_int_value("duration_ns", self.duration_ns)
        writer.write_str_value("failure_reason", self.failure_reason)
        writer.write_str_value("failure_stage", self.failure_stage)
        writer.write_str_value("id", self.id)
        writer.write_str_value("name", self.name)
        writer.write_str_value("namespace", self.namespace)
        writer.write_str_value("node_name", self.node_name)
        writer.write_str_value("operation", self.operation)
        writer.write_int_value("pause_ns", self.pause_ns)
        writer.write_int_value("physical_bytes", self.physical_bytes)
        writer.write_int_value("pod_ready_at_ms", self.pod_ready_at_ms)
        writer.write_int_value("pod_scheduled_at_ms", self.pod_scheduled_at_ms)
        writer.write_str_value("pod_uid", self.pod_uid)
        writer.write_bool_value("read", self.read)
        writer.write_str_value("restore_uuid", self.restore_uuid)
        writer.write_str_value("result", self.result)
        writer.write_str_value("storage_tier", self.storage_tier)
        writer.write_str_value("timestamp", self.timestamp)
        writer.write_str_value("type", self.type)
        writer.write_str_value("workload_type", self.workload_type)
        writer.write_additional_data_value(self.additional_data)
    

