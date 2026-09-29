from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .actions.actions_request_builder import ActionsRequestBuilder
    from .cedana.cedana_request_builder import CedanaRequestBuilder
    from .checkpoint.checkpoint_request_builder import CheckpointRequestBuilder
    from .checkpoints.checkpoints_request_builder import CheckpointsRequestBuilder
    from .cluster.cluster_request_builder import ClusterRequestBuilder
    from .csx.csx_request_builder import CsxRequestBuilder
    from .discover.discover_request_builder import DiscoverRequestBuilder
    from .download.download_request_builder import DownloadRequestBuilder
    from .dynamo.dynamo_request_builder import DynamoRequestBuilder
    from .events.events_request_builder import EventsRequestBuilder
    from .files.files_request_builder import FilesRequestBuilder
    from .hosts.hosts_request_builder import HostsRequestBuilder
    from .inference.inference_request_builder import InferenceRequestBuilder
    from .install.install_request_builder import InstallRequestBuilder
    from .instances.instances_request_builder import InstancesRequestBuilder
    from .jobs.jobs_request_builder import JobsRequestBuilder
    from .metrics.metrics_request_builder import MetricsRequestBuilder
    from .nodes.nodes_request_builder import NodesRequestBuilder
    from .operations.operations_request_builder import OperationsRequestBuilder
    from .otel.otel_request_builder import OtelRequestBuilder
    from .plugins.plugins_request_builder import PluginsRequestBuilder
    from .pods.pods_request_builder import PodsRequestBuilder
    from .policy.policy_request_builder import PolicyRequestBuilder
    from .pricing.pricing_request_builder import PricingRequestBuilder
    from .restore.restore_request_builder import RestoreRequestBuilder
    from .restores.restores_request_builder import RestoresRequestBuilder
    from .slurm.slurm_request_builder import SlurmRequestBuilder
    from .user.user_request_builder import UserRequestBuilder

class V1RequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new V1RequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1", path_parameters)
    
    @property
    def actions(self) -> ActionsRequestBuilder:
        """
        The actions property
        """
        from .actions.actions_request_builder import ActionsRequestBuilder

        return ActionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cedana(self) -> CedanaRequestBuilder:
        """
        The cedana property
        """
        from .cedana.cedana_request_builder import CedanaRequestBuilder

        return CedanaRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    def cluster(self) -> ClusterRequestBuilder:
        """
        The cluster property
        """
        from .cluster.cluster_request_builder import ClusterRequestBuilder

        return ClusterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def csx(self) -> CsxRequestBuilder:
        """
        The csx property
        """
        from .csx.csx_request_builder import CsxRequestBuilder

        return CsxRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def discover(self) -> DiscoverRequestBuilder:
        """
        The discover property
        """
        from .discover.discover_request_builder import DiscoverRequestBuilder

        return DiscoverRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def download(self) -> DownloadRequestBuilder:
        """
        The download property
        """
        from .download.download_request_builder import DownloadRequestBuilder

        return DownloadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dynamo(self) -> DynamoRequestBuilder:
        """
        The dynamo property
        """
        from .dynamo.dynamo_request_builder import DynamoRequestBuilder

        return DynamoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def events(self) -> EventsRequestBuilder:
        """
        The events property
        """
        from .events.events_request_builder import EventsRequestBuilder

        return EventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def files(self) -> FilesRequestBuilder:
        """
        The files property
        """
        from .files.files_request_builder import FilesRequestBuilder

        return FilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hosts(self) -> HostsRequestBuilder:
        """
        The hosts property
        """
        from .hosts.hosts_request_builder import HostsRequestBuilder

        return HostsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def inference(self) -> InferenceRequestBuilder:
        """
        The inference property
        """
        from .inference.inference_request_builder import InferenceRequestBuilder

        return InferenceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def install(self) -> InstallRequestBuilder:
        """
        The install property
        """
        from .install.install_request_builder import InstallRequestBuilder

        return InstallRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def instances(self) -> InstancesRequestBuilder:
        """
        The instances property
        """
        from .instances.instances_request_builder import InstancesRequestBuilder

        return InstancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def jobs(self) -> JobsRequestBuilder:
        """
        The jobs property
        """
        from .jobs.jobs_request_builder import JobsRequestBuilder

        return JobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def metrics(self) -> MetricsRequestBuilder:
        """
        The metrics property
        """
        from .metrics.metrics_request_builder import MetricsRequestBuilder

        return MetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def nodes(self) -> NodesRequestBuilder:
        """
        The nodes property
        """
        from .nodes.nodes_request_builder import NodesRequestBuilder

        return NodesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> OperationsRequestBuilder:
        """
        The operations property
        """
        from .operations.operations_request_builder import OperationsRequestBuilder

        return OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def otel(self) -> OtelRequestBuilder:
        """
        The otel property
        """
        from .otel.otel_request_builder import OtelRequestBuilder

        return OtelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def plugins(self) -> PluginsRequestBuilder:
        """
        The plugins property
        """
        from .plugins.plugins_request_builder import PluginsRequestBuilder

        return PluginsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pods(self) -> PodsRequestBuilder:
        """
        The pods property
        """
        from .pods.pods_request_builder import PodsRequestBuilder

        return PodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def policy(self) -> PolicyRequestBuilder:
        """
        The policy property
        """
        from .policy.policy_request_builder import PolicyRequestBuilder

        return PolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pricing(self) -> PricingRequestBuilder:
        """
        The pricing property
        """
        from .pricing.pricing_request_builder import PricingRequestBuilder

        return PricingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore(self) -> RestoreRequestBuilder:
        """
        The restore property
        """
        from .restore.restore_request_builder import RestoreRequestBuilder

        return RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restores(self) -> RestoresRequestBuilder:
        """
        The restores property
        """
        from .restores.restores_request_builder import RestoresRequestBuilder

        return RestoresRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def slurm(self) -> SlurmRequestBuilder:
        """
        The slurm property
        """
        from .slurm.slurm_request_builder import SlurmRequestBuilder

        return SlurmRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user(self) -> UserRequestBuilder:
        """
        The user property
        """
        from .user.user_request_builder import UserRequestBuilder

        return UserRequestBuilder(self.request_adapter, self.path_parameters)
    

