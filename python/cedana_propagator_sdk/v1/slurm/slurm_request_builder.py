from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .checkpoint.checkpoint_request_builder import CheckpointRequestBuilder
    from .checkpoints.checkpoints_request_builder import CheckpointsRequestBuilder
    from .clusters.clusters_request_builder import ClustersRequestBuilder
    from .events.events_request_builder import EventsRequestBuilder
    from .jobs.jobs_request_builder import JobsRequestBuilder
    from .maintenance_window.maintenance_window_request_builder import Maintenance_windowRequestBuilder
    from .nodes.nodes_request_builder import NodesRequestBuilder
    from .partitions.partitions_request_builder import PartitionsRequestBuilder
    from .restore.restore_request_builder import RestoreRequestBuilder

class SlurmRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/slurm
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SlurmRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/slurm", path_parameters)
    
    @property
    def checkpoint(self) -> CheckpointRequestBuilder:
        """
        The checkpoint property
        """
        from .checkpoint.checkpoint_request_builder import CheckpointRequestBuilder

        return CheckpointRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def checkpoints(self) -> CheckpointsRequestBuilder:
        """
        The checkpoints property
        """
        from .checkpoints.checkpoints_request_builder import CheckpointsRequestBuilder

        return CheckpointsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def clusters(self) -> ClustersRequestBuilder:
        """
        The clusters property
        """
        from .clusters.clusters_request_builder import ClustersRequestBuilder

        return ClustersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def events(self) -> EventsRequestBuilder:
        """
        The events property
        """
        from .events.events_request_builder import EventsRequestBuilder

        return EventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def jobs(self) -> JobsRequestBuilder:
        """
        The jobs property
        """
        from .jobs.jobs_request_builder import JobsRequestBuilder

        return JobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def maintenance_window(self) -> Maintenance_windowRequestBuilder:
        """
        The maintenance_window property
        """
        from .maintenance_window.maintenance_window_request_builder import Maintenance_windowRequestBuilder

        return Maintenance_windowRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def nodes(self) -> NodesRequestBuilder:
        """
        The nodes property
        """
        from .nodes.nodes_request_builder import NodesRequestBuilder

        return NodesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def partitions(self) -> PartitionsRequestBuilder:
        """
        The partitions property
        """
        from .partitions.partitions_request_builder import PartitionsRequestBuilder

        return PartitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore(self) -> RestoreRequestBuilder:
        """
        The restore property
        """
        from .restore.restore_request_builder import RestoreRequestBuilder

        return RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    

