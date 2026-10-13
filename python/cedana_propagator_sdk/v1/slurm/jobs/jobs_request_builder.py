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
    from ....models.http_error import HttpError
    from ....models.paginated_slurm_job_response import PaginatedSlurmJobResponse
    from .sync.sync_request_builder import SyncRequestBuilder

class JobsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/slurm/jobs
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new JobsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/slurm/jobs{?ascending*,cluster_id*,id*,job_name*,limit*,offset*,sort*,status*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[JobsRequestBuilderGetQueryParameters]] = None) -> Optional[PaginatedSlurmJobResponse]:
        """
        Paginated. `total_count` is the number of jobs matching the filters before paging.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PaginatedSlurmJobResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": HttpError,
            "500": HttpError,
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.paginated_slurm_job_response import PaginatedSlurmJobResponse

        return await self.request_adapter.send_async(request_info, PaginatedSlurmJobResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[JobsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Paginated. `total_count` is the number of jobs matching the filters before paging.
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
    def sync(self) -> SyncRequestBuilder:
        """
        The sync property
        """
        from .sync.sync_request_builder import SyncRequestBuilder

        return SyncRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class JobsRequestBuilderGetQueryParameters():
        """
        Paginated. `total_count` is the number of jobs matching the filters before paging.
        """
        # Sort ascending (default: false)
        ascending: Optional[bool] = None

        # Only return jobs belonging to this cluster
        cluster_id: Optional[UUID] = None

        # Exact SLURM job id to fetch; when set, all other filters are ignored
        id: Optional[int] = None

        # Job name or job id to query against (uses postgres ILIKE pattern search)
        job_name: Optional[str] = None

        # Page size (default 50, max 500)
        limit: Optional[int] = None

        # Row offset (default 0)
        offset: Optional[int] = None

        # One of: id, name, status, submit_time, start_time (default: start_time)
        sort: Optional[str] = None

        status: Optional[str] = None

    
    @dataclass
    class JobsRequestBuilderGetRequestConfiguration(RequestConfiguration[JobsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

