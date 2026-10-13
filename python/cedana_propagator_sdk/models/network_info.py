from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .network_info_rdma_resources import NetworkInfo_rdma_resources

@dataclass
class NetworkInfo(AdditionalDataHolder, Parsable):
    """
    Networking of one node: NICs, RDMA and the devices plugins expose for them.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Whether the NVIDIA Network Operator manages this node's NIC drivers
    network_operator: Optional[bool] = None
    # High-performance NIC vendors seen on the PCI bus, e.g. ["NVIDIA Mellanox"] (Node Feature Discovery)
    nic_vendors: Optional[list[str]] = None
    # Whether the RDMA kernel modules are loaded (Node Feature Discovery)
    rdma_available: Optional[bool] = None
    # Whether an RDMA-capable NIC is present (Node Feature Discovery)
    rdma_capable: Optional[bool] = None
    # RDMA, InfiniBand, SR-IOV and EFA devices the node advertises, by resource name, e.g. {"rdma/ib": 8}
    rdma_resources: Optional[NetworkInfo_rdma_resources] = None
    # Whether a NIC supports SR-IOV (Node Feature Discovery)
    sriov_capable: Optional[bool] = None
    # Whether SR-IOV virtual functions are configured (Node Feature Discovery)
    sriov_configured: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NetworkInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NetworkInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NetworkInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .network_info_rdma_resources import NetworkInfo_rdma_resources

        from .network_info_rdma_resources import NetworkInfo_rdma_resources

        fields: dict[str, Callable[[Any], None]] = {
            "network_operator": lambda n : setattr(self, 'network_operator', n.get_bool_value()),
            "nic_vendors": lambda n : setattr(self, 'nic_vendors', n.get_collection_of_primitive_values(str)),
            "rdma_available": lambda n : setattr(self, 'rdma_available', n.get_bool_value()),
            "rdma_capable": lambda n : setattr(self, 'rdma_capable', n.get_bool_value()),
            "rdma_resources": lambda n : setattr(self, 'rdma_resources', n.get_object_value(NetworkInfo_rdma_resources)),
            "sriov_capable": lambda n : setattr(self, 'sriov_capable', n.get_bool_value()),
            "sriov_configured": lambda n : setattr(self, 'sriov_configured', n.get_bool_value()),
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
        writer.write_bool_value("network_operator", self.network_operator)
        writer.write_collection_of_primitive_values("nic_vendors", self.nic_vendors)
        writer.write_bool_value("rdma_available", self.rdma_available)
        writer.write_bool_value("rdma_capable", self.rdma_capable)
        writer.write_object_value("rdma_resources", self.rdma_resources)
        writer.write_bool_value("sriov_capable", self.sriov_capable)
        writer.write_bool_value("sriov_configured", self.sriov_configured)
        writer.write_additional_data_value(self.additional_data)
    

