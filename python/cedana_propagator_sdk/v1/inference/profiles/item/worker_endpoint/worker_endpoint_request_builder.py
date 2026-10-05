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
from warnings import warn

if TYPE_CHECKING:
    from ......models.http_error import HttpError
    from ......models.report_worker_endpoint import ReportWorkerEndpoint

class WorkerEndpointRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/inference/profiles/{profile_id}/worker-endpoint
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WorkerEndpointRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/inference/profiles/{profile_id}/worker-endpoint", path_parameters)
    
    async def put(self,body: ReportWorkerEndpoint, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Record where a profile's worker publishes its metrics (controller only). Thepropagator can reach the port but cannot find the pod IP itself.
        param body: Where a profile's worker publishes engine metrics (controller only), plusthe KV cache facts the controller lifts off that endpoint on its ownscrape. The KV fields are optional so the endpoint-only report (sent perreconcile, before any scrape has run) never erases values a metrics scrapealready wrote.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ......models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def to_put_request_information(self,body: ReportWorkerEndpoint, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Record where a profile's worker publishes its metrics (controller only). Thepropagator can reach the port but cannot find the pod IP itself.
        param body: Where a profile's worker publishes engine metrics (controller only), plusthe KV cache facts the controller lifts off that endpoint on its ownscrape. The KV fields are optional so the endpoint-only report (sent perreconcile, before any scrape has run) never erases values a metrics scrapealready wrote.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> WorkerEndpointRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WorkerEndpointRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WorkerEndpointRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WorkerEndpointRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

