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
from warnings import warn

if TYPE_CHECKING:
    from ....models.http_error import HttpError
    from ....models.lifecycle_envelope import LifecycleEnvelope
    from ....models.lifecycle_event_view import LifecycleEventView

class LifecycleEventsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/inference/lifecycle-events
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new LifecycleEventsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/inference/lifecycle-events{?limit*,profile_id*,since*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[LifecycleEventsRequestBuilderGetQueryParameters]] = None) -> Optional[list[LifecycleEventView]]:
        """
        The cluster's recent lifecycle events across all profiles, time-ascending, so aUI can replay how the routing topology changed over time.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[LifecycleEventView]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": HttpError,
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.lifecycle_event_view import LifecycleEventView

        return await self.request_adapter.send_collection_async(request_info, LifecycleEventView, error_mapping)
    
    async def post(self,body: LifecycleEnvelope, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Documented at /inference/lifecycle-events (same collection as the GET) sogenerated SDKs get a single builder with both methods; the legacy/inference/lifecycle/events path collides with it under kiota's namesanitization, dropping the POST from the SDK. The legacy path staysregistered as an undocumented alias in api.rs for older clients.
        param body: Shared envelope for trusted lifecycle events.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": HttpError,
            "401": HttpError,
            "409": HttpError,
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[LifecycleEventsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The cluster's recent lifecycle events across all profiles, time-ascending, so aUI can replay how the routing topology changed over time.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: LifecycleEnvelope, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Documented at /inference/lifecycle-events (same collection as the GET) sogenerated SDKs get a single builder with both methods; the legacy/inference/lifecycle/events path collides with it under kiota's namesanitization, dropping the POST from the SDK. The legacy path staysregistered as an undocumented alias in api.rs for older clients.
        param body: Shared envelope for trusted lifecycle events.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> LifecycleEventsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: LifecycleEventsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return LifecycleEventsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class LifecycleEventsRequestBuilderGetQueryParameters():
        """
        The cluster's recent lifecycle events across all profiles, time-ascending, so aUI can replay how the routing topology changed over time.
        """
        limit: Optional[int] = None

        # Only this profile's events.
        profile_id: Optional[str] = None

        # Only events at or after this instant, so a poller can page forward.
        since: Optional[datetime.datetime] = None

    
    @dataclass
    class LifecycleEventsRequestBuilderGetRequestConfiguration(RequestConfiguration[LifecycleEventsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class LifecycleEventsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

