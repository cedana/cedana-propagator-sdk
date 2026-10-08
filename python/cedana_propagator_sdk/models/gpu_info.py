from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .gpu_info_mig_devices import GpuInfo_mig_devices

@dataclass
class GpuInfo(AdditionalDataHolder, Parsable):
    """
    GPU inventory of one node.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # nvidia.com/gpu the scheduler can hand out (excludes MIG slices)
    allocatable: Optional[int] = None
    # Compute capability, e.g. "9.0"
    compute_capability: Optional[str] = None
    # Physical GPUs on the node
    count: Optional[int] = None
    # Highest CUDA version the driver supports, e.g. "12.4"
    cuda_version: Optional[str] = None
    # NVIDIA driver version, e.g. "550.54.15"
    driver_version: Optional[str] = None
    # Architecture family, e.g. "hopper"
    family: Optional[str] = None
    # Memory per GPU in MiB
    memory_mib: Optional[int] = None
    # Allocatable MIG slices by profile, e.g. {"1g.10gb": 7}; empty when MIG is off
    mig_devices: Optional[GpuInfo_mig_devices] = None
    # MIG strategy ("none", "single" or "mixed"), or "disabled" when mig-manager has MIG off
    mig_strategy: Optional[str] = None
    # GPU model, e.g. "NVIDIA-H100-80GB-HBM3"
    product: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GpuInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GpuInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GpuInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .gpu_info_mig_devices import GpuInfo_mig_devices

        from .gpu_info_mig_devices import GpuInfo_mig_devices

        fields: dict[str, Callable[[Any], None]] = {
            "allocatable": lambda n : setattr(self, 'allocatable', n.get_int_value()),
            "compute_capability": lambda n : setattr(self, 'compute_capability', n.get_str_value()),
            "count": lambda n : setattr(self, 'count', n.get_int_value()),
            "cuda_version": lambda n : setattr(self, 'cuda_version', n.get_str_value()),
            "driver_version": lambda n : setattr(self, 'driver_version', n.get_str_value()),
            "family": lambda n : setattr(self, 'family', n.get_str_value()),
            "memory_mib": lambda n : setattr(self, 'memory_mib', n.get_int_value()),
            "mig_devices": lambda n : setattr(self, 'mig_devices', n.get_object_value(GpuInfo_mig_devices)),
            "mig_strategy": lambda n : setattr(self, 'mig_strategy', n.get_str_value()),
            "product": lambda n : setattr(self, 'product', n.get_str_value()),
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
        writer.write_int_value("allocatable", self.allocatable)
        writer.write_str_value("compute_capability", self.compute_capability)
        writer.write_int_value("count", self.count)
        writer.write_str_value("cuda_version", self.cuda_version)
        writer.write_str_value("driver_version", self.driver_version)
        writer.write_str_value("family", self.family)
        writer.write_int_value("memory_mib", self.memory_mib)
        writer.write_object_value("mig_devices", self.mig_devices)
        writer.write_str_value("mig_strategy", self.mig_strategy)
        writer.write_str_value("product", self.product)
        writer.write_additional_data_value(self.additional_data)
    

