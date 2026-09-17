from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID
from warnings import warn

if TYPE_CHECKING:
    from ...models.cluster import Cluster
    from ...models.create_cluster_request import CreateClusterRequest
    from ...models.http_error import HttpError
    from .count.count_request_builder import CountRequestBuilder
    from .item.cluster_item_request_builder import ClusterItemRequestBuilder
    from .sync.sync_request_builder import SyncRequestBuilder
    from .workload.workload_request_builder import WorkloadRequestBuilder

class ClusterRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/cluster
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ClusterRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/cluster{?kind*}", path_parameters)
    
    def by_id(self,id: UUID) -> ClusterItemRequestBuilder:
        """
        Gets an item from the cedana_propagator_sdk.v1.cluster.item collection
        param id: Unique identifier of the item
        Returns: ClusterItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.cluster_item_request_builder import ClusterItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return ClusterItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ClusterRequestBuilderGetQueryParameters]] = None) -> Optional[list[Cluster]]:
        """
        Returns all clusters. Optional `?kind=kubernetes|slurm` filter.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[Cluster]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": HttpError,
            "500": HttpError,
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.cluster import Cluster

        return await self.request_adapter.send_collection_async(request_info, Cluster, error_mapping)
    
    async def post(self,body: CreateClusterRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[str]:
        """
        Creates or updates info regarding a Kubernetes cluster
        param body: CreateClusterRequest is the request body for creating a cluster
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[str]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ...models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": HttpError,
            "500": HttpError,
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "str", error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ClusterRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns all clusters. Optional `?kind=kubernetes|slurm` filter.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: CreateClusterRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates or updates info regarding a Kubernetes cluster
        param body: CreateClusterRequest is the request body for creating a cluster
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "text/plain;q=0.9")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> ClusterRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ClusterRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ClusterRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        The count property
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sync(self) -> SyncRequestBuilder:
        """
        The sync property
        """
        from .sync.sync_request_builder import SyncRequestBuilder

        return SyncRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def workload(self) -> WorkloadRequestBuilder:
        """
        The workload property
        """
        from .workload.workload_request_builder import WorkloadRequestBuilder

        return WorkloadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ClusterRequestBuilderGetQueryParameters():
        """
        Returns all clusters. Optional `?kind=kubernetes|slurm` filter.
        """
        # Filter by cluster kind: "kubernetes" or "slurm"
        kind: Optional[str] = None

    
    @dataclass
    class ClusterRequestBuilderGetRequestConfiguration(RequestConfiguration[ClusterRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ClusterRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

