from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SlurmJob(AdditionalDataHolder, Parsable):
    """
    SlurmJob represents a SLURM job stored in the database
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The account property
    account: Optional[str] = None
    # The cedana_enabled property
    cedana_enabled: Optional[bool] = None
    # The cluster_id property
    cluster_id: Optional[str] = None
    # Numeric derived exit code (slurmdbd derived_ec — uint32, widened to i64)
    derived_ec: Optional[int] = None
    # Human-readable exit reason (e.g. "Preempted by higher-priority job")
    derived_es: Optional[str] = None
    # Unix epoch seconds; 0 means not yet ended
    end_time: Optional[int] = None
    # The exit_code property
    exit_code: Optional[int] = None
    # Node that triggered job failure, if any
    failed_node: Optional[str] = None
    # The id property
    id: Optional[int] = None
    # The job_id property
    job_id: Optional[int] = None
    # UID that issued the kill/preempt signal (uid_t / uint32, widened to i64)
    kill_requid: Optional[int] = None
    # The name property
    name: Optional[str] = None
    # The nodes property
    nodes: Optional[str] = None
    # The num_cpus property
    num_cpus: Optional[int] = None
    # The num_nodes property
    num_nodes: Optional[int] = None
    # The partition property
    partition: Optional[str] = None
    # The priority property
    priority: Optional[int] = None
    # Unix epoch seconds; 0 means not set
    start_time: Optional[int] = None
    # Reason code for prior state transition
    state_reason_prev: Optional[int] = None
    # The status property
    status: Optional[str] = None
    # Unix epoch seconds; 0 means not set
    submit_time: Optional[int] = None
    # Seconds the job spent suspended
    time_suspended: Optional[int] = None
    # The work_dir property
    work_dir: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SlurmJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SlurmJob
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SlurmJob()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "account": lambda n : setattr(self, 'account', n.get_str_value()),
            "cedana_enabled": lambda n : setattr(self, 'cedana_enabled', n.get_bool_value()),
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_str_value()),
            "derived_ec": lambda n : setattr(self, 'derived_ec', n.get_int_value()),
            "derived_es": lambda n : setattr(self, 'derived_es', n.get_str_value()),
            "end_time": lambda n : setattr(self, 'end_time', n.get_int_value()),
            "exit_code": lambda n : setattr(self, 'exit_code', n.get_int_value()),
            "failed_node": lambda n : setattr(self, 'failed_node', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "job_id": lambda n : setattr(self, 'job_id', n.get_int_value()),
            "kill_requid": lambda n : setattr(self, 'kill_requid', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "nodes": lambda n : setattr(self, 'nodes', n.get_str_value()),
            "num_cpus": lambda n : setattr(self, 'num_cpus', n.get_int_value()),
            "num_nodes": lambda n : setattr(self, 'num_nodes', n.get_int_value()),
            "partition": lambda n : setattr(self, 'partition', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "start_time": lambda n : setattr(self, 'start_time', n.get_int_value()),
            "state_reason_prev": lambda n : setattr(self, 'state_reason_prev', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "submit_time": lambda n : setattr(self, 'submit_time', n.get_int_value()),
            "time_suspended": lambda n : setattr(self, 'time_suspended', n.get_int_value()),
            "work_dir": lambda n : setattr(self, 'work_dir', n.get_str_value()),
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
        writer.write_str_value("account", self.account)
        writer.write_bool_value("cedana_enabled", self.cedana_enabled)
        writer.write_str_value("cluster_id", self.cluster_id)
        writer.write_int_value("derived_ec", self.derived_ec)
        writer.write_str_value("derived_es", self.derived_es)
        writer.write_int_value("end_time", self.end_time)
        writer.write_int_value("exit_code", self.exit_code)
        writer.write_str_value("failed_node", self.failed_node)
        writer.write_int_value("id", self.id)
        writer.write_int_value("job_id", self.job_id)
        writer.write_int_value("kill_requid", self.kill_requid)
        writer.write_str_value("name", self.name)
        writer.write_str_value("nodes", self.nodes)
        writer.write_int_value("num_cpus", self.num_cpus)
        writer.write_int_value("num_nodes", self.num_nodes)
        writer.write_str_value("partition", self.partition)
        writer.write_int_value("priority", self.priority)
        writer.write_int_value("start_time", self.start_time)
        writer.write_int_value("state_reason_prev", self.state_reason_prev)
        writer.write_str_value("status", self.status)
        writer.write_int_value("submit_time", self.submit_time)
        writer.write_int_value("time_suspended", self.time_suspended)
        writer.write_str_value("work_dir", self.work_dir)
        writer.write_additional_data_value(self.additional_data)
    

