from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .checkpoint_cpu.checkpoint_cpu_request_builder import CheckpointCpuRequestBuilder
    from .checkpoint_savings.checkpoint_savings_request_builder import CheckpointSavingsRequestBuilder
    from .export.export_request_builder import ExportRequestBuilder
    from .gpu.gpu_request_builder import GpuRequestBuilder
    from .ingest.ingest_request_builder import IngestRequestBuilder
    from .k8.k8_request_builder import K8RequestBuilder
    from .operations.operations_request_builder import OperationsRequestBuilder
    from .pods.pods_request_builder import PodsRequestBuilder
    from .slurm.slurm_request_builder import SlurmRequestBuilder

class MetricsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/metrics
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MetricsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/metrics", path_parameters)
    
    @property
    def checkpoint_cpu(self) -> CheckpointCpuRequestBuilder:
        """
        The checkpointCpu property
        """
        from .checkpoint_cpu.checkpoint_cpu_request_builder import CheckpointCpuRequestBuilder

        return CheckpointCpuRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def checkpoint_savings(self) -> CheckpointSavingsRequestBuilder:
        """
        The checkpointSavings property
        """
        from .checkpoint_savings.checkpoint_savings_request_builder import CheckpointSavingsRequestBuilder

        return CheckpointSavingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def export(self) -> ExportRequestBuilder:
        """
        The export property
        """
        from .export.export_request_builder import ExportRequestBuilder

        return ExportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gpu(self) -> GpuRequestBuilder:
        """
        The gpu property
        """
        from .gpu.gpu_request_builder import GpuRequestBuilder

        return GpuRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ingest(self) -> IngestRequestBuilder:
        """
        The ingest property
        """
        from .ingest.ingest_request_builder import IngestRequestBuilder

        return IngestRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def k8(self) -> K8RequestBuilder:
        """
        The k8 property
        """
        from .k8.k8_request_builder import K8RequestBuilder

        return K8RequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> OperationsRequestBuilder:
        """
        The operations property
        """
        from .operations.operations_request_builder import OperationsRequestBuilder

        return OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pods(self) -> PodsRequestBuilder:
        """
        The pods property
        """
        from .pods.pods_request_builder import PodsRequestBuilder

        return PodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def slurm(self) -> SlurmRequestBuilder:
        """
        The slurm property
        """
        from .slurm.slurm_request_builder import SlurmRequestBuilder

        return SlurmRequestBuilder(self.request_adapter, self.path_parameters)
    

