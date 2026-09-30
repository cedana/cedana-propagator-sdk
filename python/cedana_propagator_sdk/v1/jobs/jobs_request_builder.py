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
    from ...models.paginated_job_response import PaginatedJobResponse
    from .by_priority.by_priority_request_builder import ByPriorityRequestBuilder
    from .count.count_request_builder import CountRequestBuilder
    from .filter.filter_request_builder import FilterRequestBuilder
    from .item.with_job_item_request_builder import WithJob_ItemRequestBuilder
    from .namespaces.namespaces_request_builder import NamespacesRequestBuilder
    from .priorities.priorities_request_builder import PrioritiesRequestBuilder
    from .statuses.statuses_request_builder import StatusesRequestBuilder

class JobsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/jobs
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new JobsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/jobs{?ascending*,cluster_id*,job_name*,limit*,namespace*,offset*,sort*,status*}", path_parameters)
    
    def by_job_id(self,job_id: UUID) -> WithJob_ItemRequestBuilder:
        """
        Gets an item from the cedana_propagator_sdk.v1.jobs.item collection
        param job_id: Job ID to get pods for
        Returns: WithJob_ItemRequestBuilder
        """
        if job_id is None:
            raise TypeError("job_id cannot be null.")
        from .item.with_job_item_request_builder import WithJob_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["job_id"] = job_id
        return WithJob_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[JobsRequestBuilderGetQueryParameters]] = None) -> Optional[PaginatedJobResponse]:
        """
        Paginated. Only returns jobs from clusters with status 'active'. `cluster_id` scopes both thejobs and the available filters to one cluster.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PaginatedJobResponse]
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
        from ...models.paginated_job_response import PaginatedJobResponse

        return await self.request_adapter.send_async(request_info, PaginatedJobResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[JobsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Paginated. Only returns jobs from clusters with status 'active'. `cluster_id` scopes both thejobs and the available filters to one cluster.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> JobsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: JobsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return JobsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def by_priority(self) -> ByPriorityRequestBuilder:
        """
        The byPriority property
        """
        from .by_priority.by_priority_request_builder import ByPriorityRequestBuilder

        return ByPriorityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        The count property
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def filter(self) -> FilterRequestBuilder:
        """
        The filter property
        """
        from .filter.filter_request_builder import FilterRequestBuilder

        return FilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def namespaces(self) -> NamespacesRequestBuilder:
        """
        The namespaces property
        """
        from .namespaces.namespaces_request_builder import NamespacesRequestBuilder

        return NamespacesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def priorities(self) -> PrioritiesRequestBuilder:
        """
        The priorities property
        """
        from .priorities.priorities_request_builder import PrioritiesRequestBuilder

        return PrioritiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def statuses(self) -> StatusesRequestBuilder:
        """
        The statuses property
        """
        from .statuses.statuses_request_builder import StatusesRequestBuilder

        return StatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class JobsRequestBuilderGetQueryParameters():
        """
        Paginated. Only returns jobs from clusters with status 'active'. `cluster_id` scopes both thejobs and the available filters to one cluster.
        """
        # Sort ascending (default false)
        ascending: Optional[bool] = None

        # Only return jobs belonging to this cluster
        cluster_id: Optional[UUID] = None

        # job name to query against (uses postgres ILIKE pattern search)
        job_name: Optional[str] = None

        # Page size (default 50, max 500)
        limit: Optional[int] = None

        namespace: Optional[str] = None

        # Row offset (default 0)
        offset: Optional[int] = None

        # Sort column: `id`, `name`, `namespace`, `status` or `start_time` (default `start_time`)
        sort: Optional[str] = None

        status: Optional[str] = None

    
    @dataclass
    class JobsRequestBuilderGetRequestConfiguration(RequestConfiguration[JobsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

