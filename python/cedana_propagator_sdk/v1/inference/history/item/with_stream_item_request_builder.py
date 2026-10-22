from __future__ import annotations
import datetime
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
    from .....models.history_page import HistoryPage
    from .....models.http_error import HttpError

class WithStreamItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/inference/history/{stream}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithStreamItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/inference/history/{stream}?since={since}&until={until}{&after_id*,after_time*,cluster_id*,limit*,profile_id*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WithStreamItemRequestBuilderGetQueryParameters]] = None) -> Optional[HistoryPage]:
        """
        Replays lifecycle, placement, or request records in stable timestamp/id order,falling back to ingestion time. Late arrivals can precede a cursor: re-exportafter telemetry drains.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[HistoryPage]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": HttpError,
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.history_page import HistoryPage

        return await self.request_adapter.send_async(request_info, HistoryPage, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WithStreamItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Replays lifecycle, placement, or request records in stable timestamp/id order,falling back to ingestion time. Late arrivals can precede a cursor: re-exportafter telemetry drains.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithStreamItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithStreamItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithStreamItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithStreamItemRequestBuilderGetQueryParameters():
        """
        Replays lifecycle, placement, or request records in stable timestamp/id order,falling back to ingestion time. Late arrivals can precede a cursor: re-exportafter telemetry drains.
        """
        after_id: Optional[UUID] = None

        after_time: Optional[datetime.datetime] = None

        # Applicable to lifecycle and placement; requests have no cluster identity.
        cluster_id: Optional[UUID] = None

        limit: Optional[int] = None

        profile_id: Optional[str] = None

        since: Optional[datetime.datetime] = None

        # Exclusive end of the recording window. Keep fixed while paging.
        until: Optional[datetime.datetime] = None

    
    @dataclass
    class WithStreamItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WithStreamItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

