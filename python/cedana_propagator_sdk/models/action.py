from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class Action(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The action_id property
    action_id: Optional[UUID] = None
    # The action_timestamp property
    action_timestamp: Optional[datetime.datetime] = None
    # The checkpoint_completed_timestamp property
    checkpoint_completed_timestamp: Optional[datetime.datetime] = None
    # The checkpoint_id property
    checkpoint_id: Optional[UUID] = None
    # The checkpoint's CEDANA_CHECKPOINT name (the env value it restores from),used to group automatic/named checkpoints. Null for unnamed checkpoints.
    checkpoint_name: Optional[str] = None
    # The checkpoint_status property
    checkpoint_status: Optional[str] = None
    # Whether the checkpoint is a (GPU delta) increment. Authoritative evenwhen parent_checkpoint_id is null (malformed id at ingest, parent deleted)
    delta: Optional[bool] = None
    # The gpu property
    gpu: Optional[str] = None
    # The node_name property
    node_name: Optional[str] = None
    # Checkpoint this one is an increment of; null for full checkpoints andfor deltas whose parent is unknown or deleted
    parent_checkpoint_id: Optional[UUID] = None
    # The platform property
    platform: Optional[str] = None
    # The reason property
    reason: Optional[str] = None
    # The status property
    status: Optional[str] = None
    # The total_duration property
    total_duration: Optional[int] = None
    # The total_io property
    total_io: Optional[int] = None
    # The type property
    type: Optional[str] = None
    # Owning workload kind of the checkpointed pod: "DynamoGraphDeployment" whenthe pod belongs to a Dynamo deployment, else the pod's immediateownerReferences kind (ReplicaSet/Job/StatefulSet…). Null if unknown.
    workload_kind: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Action:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Action
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Action()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "action_id": lambda n : setattr(self, 'action_id', n.get_uuid_value()),
            "action_timestamp": lambda n : setattr(self, 'action_timestamp', n.get_datetime_value()),
            "checkpoint_completed_timestamp": lambda n : setattr(self, 'checkpoint_completed_timestamp', n.get_datetime_value()),
            "checkpoint_id": lambda n : setattr(self, 'checkpoint_id', n.get_uuid_value()),
            "checkpoint_name": lambda n : setattr(self, 'checkpoint_name', n.get_str_value()),
            "checkpoint_status": lambda n : setattr(self, 'checkpoint_status', n.get_str_value()),
            "delta": lambda n : setattr(self, 'delta', n.get_bool_value()),
            "gpu": lambda n : setattr(self, 'gpu', n.get_str_value()),
            "node_name": lambda n : setattr(self, 'node_name', n.get_str_value()),
            "parent_checkpoint_id": lambda n : setattr(self, 'parent_checkpoint_id', n.get_uuid_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "total_duration": lambda n : setattr(self, 'total_duration', n.get_int_value()),
            "total_io": lambda n : setattr(self, 'total_io', n.get_int_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "workload_kind": lambda n : setattr(self, 'workload_kind', n.get_str_value()),
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
        writer.write_uuid_value("action_id", self.action_id)
        writer.write_datetime_value("action_timestamp", self.action_timestamp)
        writer.write_datetime_value("checkpoint_completed_timestamp", self.checkpoint_completed_timestamp)
        writer.write_uuid_value("checkpoint_id", self.checkpoint_id)
        writer.write_str_value("checkpoint_name", self.checkpoint_name)
        writer.write_str_value("checkpoint_status", self.checkpoint_status)
        writer.write_bool_value("delta", self.delta)
        writer.write_str_value("gpu", self.gpu)
        writer.write_str_value("node_name", self.node_name)
        writer.write_uuid_value("parent_checkpoint_id", self.parent_checkpoint_id)
        writer.write_str_value("platform", self.platform)
        writer.write_str_value("reason", self.reason)
        writer.write_str_value("status", self.status)
        writer.write_int_value("total_duration", self.total_duration)
        writer.write_int_value("total_io", self.total_io)
        writer.write_str_value("type", self.type)
        writer.write_str_value("workload_kind", self.workload_kind)
        writer.write_additional_data_value(self.additional_data)
    

