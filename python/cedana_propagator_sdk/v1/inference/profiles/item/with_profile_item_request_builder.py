from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .checkpoint.checkpoint_request_builder import CheckpointRequestBuilder
    from .hosting.hosting_request_builder import HostingRequestBuilder
    from .kvbm.kvbm_request_builder import KvbmRequestBuilder
    from .kv_cache.kv_cache_request_builder import KvCacheRequestBuilder
    from .lmcache.lmcache_request_builder import LmcacheRequestBuilder
    from .progress.progress_request_builder import ProgressRequestBuilder
    from .restart.restart_request_builder import RestartRequestBuilder
    from .restore_hints.restore_hints_request_builder import RestoreHintsRequestBuilder
    from .served_prefixes.served_prefixes_request_builder import ServedPrefixesRequestBuilder
    from .state.state_request_builder import StateRequestBuilder
    from .worker_endpoint.worker_endpoint_request_builder import WorkerEndpointRequestBuilder

class WithProfile_ItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/inference/profiles/{profile_id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithProfile_ItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/inference/profiles/{profile_id}", path_parameters)
    
    @property
    def checkpoint(self) -> CheckpointRequestBuilder:
        """
        The checkpoint property
        """
        from .checkpoint.checkpoint_request_builder import CheckpointRequestBuilder

        return CheckpointRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hosting(self) -> HostingRequestBuilder:
        """
        The hosting property
        """
        from .hosting.hosting_request_builder import HostingRequestBuilder

        return HostingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def kv_cache(self) -> KvCacheRequestBuilder:
        """
        The kvCache property
        """
        from .kv_cache.kv_cache_request_builder import KvCacheRequestBuilder

        return KvCacheRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def kvbm(self) -> KvbmRequestBuilder:
        """
        The kvbm property
        """
        from .kvbm.kvbm_request_builder import KvbmRequestBuilder

        return KvbmRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def lmcache(self) -> LmcacheRequestBuilder:
        """
        The lmcache property
        """
        from .lmcache.lmcache_request_builder import LmcacheRequestBuilder

        return LmcacheRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def progress(self) -> ProgressRequestBuilder:
        """
        The progress property
        """
        from .progress.progress_request_builder import ProgressRequestBuilder

        return ProgressRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restart(self) -> RestartRequestBuilder:
        """
        The restart property
        """
        from .restart.restart_request_builder import RestartRequestBuilder

        return RestartRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore_hints(self) -> RestoreHintsRequestBuilder:
        """
        The restoreHints property
        """
        from .restore_hints.restore_hints_request_builder import RestoreHintsRequestBuilder

        return RestoreHintsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def served_prefixes(self) -> ServedPrefixesRequestBuilder:
        """
        The servedPrefixes property
        """
        from .served_prefixes.served_prefixes_request_builder import ServedPrefixesRequestBuilder

        return ServedPrefixesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def state(self) -> StateRequestBuilder:
        """
        The state property
        """
        from .state.state_request_builder import StateRequestBuilder

        return StateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def worker_endpoint(self) -> WorkerEndpointRequestBuilder:
        """
        The workerEndpoint property
        """
        from .worker_endpoint.worker_endpoint_request_builder import WorkerEndpointRequestBuilder

        return WorkerEndpointRequestBuilder(self.request_adapter, self.path_parameters)
    

