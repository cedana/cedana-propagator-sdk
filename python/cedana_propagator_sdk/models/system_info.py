from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SystemInfo(AdditionalDataHolder, Parsable):
    """
    Memory and software of one node.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Memory the scheduler can hand out, after system reservations
    allocatable_memory_bytes: Optional[int] = None
    # e.g. "containerd://2.3.3"
    container_runtime: Optional[str] = None
    # Huge pages reserved on the node, all page sizes together; absent when none are
    hugepages_bytes: Optional[int] = None
    # The kernel_version property
    kernel_version: Optional[str] = None
    # The kubelet_version property
    kubelet_version: Optional[str] = None
    # The max_pods property
    max_pods: Optional[int] = None
    # The memory_bytes property
    memory_bytes: Optional[int] = None
    # Whether memory spans several NUMA nodes (Node Feature Discovery)
    numa: Optional[bool] = None
    # e.g. "Ubuntu 24.04.4 LTS"
    os_image: Optional[str] = None
    # The zone property
    zone: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SystemInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SystemInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SystemInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "allocatable_memory_bytes": lambda n : setattr(self, 'allocatable_memory_bytes', n.get_int_value()),
            "container_runtime": lambda n : setattr(self, 'container_runtime', n.get_str_value()),
            "hugepages_bytes": lambda n : setattr(self, 'hugepages_bytes', n.get_int_value()),
            "kernel_version": lambda n : setattr(self, 'kernel_version', n.get_str_value()),
            "kubelet_version": lambda n : setattr(self, 'kubelet_version', n.get_str_value()),
            "max_pods": lambda n : setattr(self, 'max_pods', n.get_int_value()),
            "memory_bytes": lambda n : setattr(self, 'memory_bytes', n.get_int_value()),
            "numa": lambda n : setattr(self, 'numa', n.get_bool_value()),
            "os_image": lambda n : setattr(self, 'os_image', n.get_str_value()),
            "zone": lambda n : setattr(self, 'zone', n.get_str_value()),
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
        writer.write_int_value("allocatable_memory_bytes", self.allocatable_memory_bytes)
        writer.write_str_value("container_runtime", self.container_runtime)
        writer.write_int_value("hugepages_bytes", self.hugepages_bytes)
        writer.write_str_value("kernel_version", self.kernel_version)
        writer.write_str_value("kubelet_version", self.kubelet_version)
        writer.write_int_value("max_pods", self.max_pods)
        writer.write_int_value("memory_bytes", self.memory_bytes)
        writer.write_bool_value("numa", self.numa)
        writer.write_str_value("os_image", self.os_image)
        writer.write_str_value("zone", self.zone)
        writer.write_additional_data_value(self.additional_data)
    

