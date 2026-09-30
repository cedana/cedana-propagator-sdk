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
    from ...models.paginated_checkpoint_response import PaginatedCheckpointResponse
    from .deprecate.deprecate_request_builder import DeprecateRequestBuilder
    from .info.info_request_builder import InfoRequestBuilder
    from .item.checkpoints_item_request_builder import CheckpointsItemRequestBuilder
    from .uploaded.uploaded_request_builder import UploadedRequestBuilder

class CheckpointsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/checkpoints
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CheckpointsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/checkpoints{?ascending*,cluster_id*,ids*,limit*,offset*,sort*}", path_parameters)
    
    def by_id(self,id: str) -> CheckpointsItemRequestBuilder:
        """
        Gets an item from the cedana_propagator_sdk.v1.checkpoints.item collection
        param id: Checkpoint ID
        Returns: CheckpointsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.checkpoints_item_request_builder import CheckpointsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return CheckpointsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[CheckpointsRequestBuilderGetQueryParameters]] = None) -> Optional[PaginatedCheckpointResponse]:
        """
        Paginated. `ids` (comma-separated UUIDs) and `cluster_id` (the cluster the checkpoint actionran on) filter the list; `total_count` is the number of matches before paging.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PaginatedCheckpointResponse]
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
        from ...models.paginated_checkpoint_response import PaginatedCheckpointResponse

        return await self.request_adapter.send_async(request_info, PaginatedCheckpointResponse, error_mapping)
    
    async def post(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[str]:
        """
        Builds a new checkpoint without the metadata and information about the checkpoint with status initializing
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[str]
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        from ...models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "500": HttpError,
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "str", error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CheckpointsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Paginated. `ids` (comma-separated UUIDs) and `cluster_id` (the cluster the checkpoint actionran on) filter the list; `total_count` is the number of matches before paging.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Builds a new checkpoint without the metadata and information about the checkpoint with status initializing
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "text/plain;q=0.9")
        return request_info
    
    def with_url(self,raw_url: str) -> CheckpointsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CheckpointsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CheckpointsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def deprecate(self) -> DeprecateRequestBuilder:
        """
        The deprecate property
        """
        from .deprecate.deprecate_request_builder import DeprecateRequestBuilder

        return DeprecateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def info(self) -> InfoRequestBuilder:
        """
        The info property
        """
        from .info.info_request_builder import InfoRequestBuilder

        return InfoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def uploaded(self) -> UploadedRequestBuilder:
        """
        The uploaded property
        """
        from .uploaded.uploaded_request_builder import UploadedRequestBuilder

        return UploadedRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CheckpointsRequestBuilderGetQueryParameters():
        """
        Paginated. `ids` (comma-separated UUIDs) and `cluster_id` (the cluster the checkpoint actionran on) filter the list; `total_count` is the number of matches before paging.
        """
        # Sort ascending (default false)
        ascending: Optional[bool] = None

        # Only return checkpoints whose checkpoint action ran on this cluster
        cluster_id: Optional[UUID] = None

        # Comma-separated list of checkpoint UUIDs to filter by
        ids: Optional[str] = None

        # Page size (default 50, max 500)
        limit: Optional[int] = None

        # Row offset (default 0)
        offset: Optional[int] = None

        # Sort column: `id`, `name`, `status`, `platform` or `gpu` (default `id`)
        sort: Optional[str] = None

    
    @dataclass
    class CheckpointsRequestBuilderGetRequestConfiguration(RequestConfiguration[CheckpointsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CheckpointsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

