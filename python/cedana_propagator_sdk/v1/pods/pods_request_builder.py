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
    from ...models.http_error import HttpError
    from ...models.paginated_pod_response import PaginatedPodResponse
    from .count.count_request_builder import CountRequestBuilder
    from .namespaces.namespaces_request_builder import NamespacesRequestBuilder
    from .statuses.statuses_request_builder import StatusesRequestBuilder

class PodsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/pods
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PodsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/pods{?ascending*,cluster_id*,id*,limit*,namespace*,offset*,pod_name*,sort*,status*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PodsRequestBuilderGetQueryParameters]] = None) -> Optional[PaginatedPodResponse]:
        """
        Paginated. Only returns pods from clusters with status 'active' whose node synced within thelast 5 minutes, and never pods with status 'deleted'. `cluster_id` scopes both the pods andthe available filters to one cluster. `id` looks up that single pod (still subject to`cluster_id`) and ignores the other filters.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PaginatedPodResponse]
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
        from ...models.paginated_pod_response import PaginatedPodResponse

        return await self.request_adapter.send_async(request_info, PaginatedPodResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PodsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Paginated. Only returns pods from clusters with status 'active' whose node synced within thelast 5 minutes, and never pods with status 'deleted'. `cluster_id` scopes both the pods andthe available filters to one cluster. `id` looks up that single pod (still subject to`cluster_id`) and ignores the other filters.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> PodsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PodsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PodsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        The count property
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def namespaces(self) -> NamespacesRequestBuilder:
        """
        The namespaces property
        """
        from .namespaces.namespaces_request_builder import NamespacesRequestBuilder

        return NamespacesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def statuses(self) -> StatusesRequestBuilder:
        """
        The statuses property
        """
        from .statuses.statuses_request_builder import StatusesRequestBuilder

        return StatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PodsRequestBuilderGetQueryParameters():
        """
        Paginated. Only returns pods from clusters with status 'active' whose node synced within thelast 5 minutes, and never pods with status 'deleted'. `cluster_id` scopes both the pods andthe available filters to one cluster. `id` looks up that single pod (still subject to`cluster_id`) and ignores the other filters.
        """
        # Sort ascending (default false)
        ascending: Optional[bool] = None

        # Only return pods belonging to this cluster
        cluster_id: Optional[UUID] = None

        # Exact pod id. When set, every other filter except `cluster_id` is ignored
        id: Optional[UUID] = None

        # Page size (default 50, max 500)
        limit: Optional[int] = None

        namespace: Optional[str] = None

        # Row offset (default 0)
        offset: Optional[int] = None

        # pod name to query against (uses postgres ILIKE pattern search)
        pod_name: Optional[str] = None

        # Sort column: `id`, `name`, `namespace` or `status` (default `name`)
        sort: Optional[str] = None

        status: Optional[str] = None

    
    @dataclass
    class PodsRequestBuilderGetRequestConfiguration(RequestConfiguration[PodsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

