from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CpuInfo(AdditionalDataHolder, Parsable):
    """
    CPU of one node.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # CPUs the scheduler can hand out, after system reservations
    allocatable_cores: Optional[float] = None
    # "amd64" or "arm64"
    architecture: Optional[str] = None
    # Logical CPUs on the node
    cores: Optional[float] = None
    # Whether SMT/hyper-threading is on (Node Feature Discovery)
    hyperthreading: Optional[bool] = None
    # Hypervisor the node runs under, e.g. "kvm"; newer NFD versions only
    hypervisor: Optional[str] = None
    # Highest x86-64 microarchitecture level, e.g. "x86-64-v4" (Node Feature Discovery)
    isa_level: Optional[str] = None
    # "Intel" or "AMD" (Node Feature Discovery)
    vendor: Optional[str] = None
    # Whether the node is a VM, from the CPUID hypervisor flag (Node Feature Discovery)
    virtualized: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CpuInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CpuInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CpuInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "allocatable_cores": lambda n : setattr(self, 'allocatable_cores', n.get_float_value()),
            "architecture": lambda n : setattr(self, 'architecture', n.get_str_value()),
            "cores": lambda n : setattr(self, 'cores', n.get_float_value()),
            "hyperthreading": lambda n : setattr(self, 'hyperthreading', n.get_bool_value()),
            "hypervisor": lambda n : setattr(self, 'hypervisor', n.get_str_value()),
            "isa_level": lambda n : setattr(self, 'isa_level', n.get_str_value()),
            "vendor": lambda n : setattr(self, 'vendor', n.get_str_value()),
            "virtualized": lambda n : setattr(self, 'virtualized', n.get_bool_value()),
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
        writer.write_float_value("allocatable_cores", self.allocatable_cores)
        writer.write_str_value("architecture", self.architecture)
        writer.write_float_value("cores", self.cores)
        writer.write_bool_value("hyperthreading", self.hyperthreading)
        writer.write_str_value("hypervisor", self.hypervisor)
        writer.write_str_value("isa_level", self.isa_level)
        writer.write_str_value("vendor", self.vendor)
        writer.write_bool_value("virtualized", self.virtualized)
        writer.write_additional_data_value(self.additional_data)
    

