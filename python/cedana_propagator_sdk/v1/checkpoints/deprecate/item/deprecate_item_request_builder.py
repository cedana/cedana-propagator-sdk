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
    from .....models.http_error import HttpError

class DeprecateItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/checkpoints/deprecate/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DeprecateItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/checkpoints/deprecate/{id}", path_parameters)
    
    async def patch(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[str]:
        """
        Has a helper on the checkpoint's cluster delete its files (chosen as for the filesendpoints: any helper for a remote checkpoint, the node holding it for a local one),then marks the checkpoint deprecated. A checkpoint without a path has no files todelete and is just deprecated. One with files but no cluster to ask (not takenthrough a checkpoint action) is kept, with a 409, rather than deprecated with itsfiles left behind. If the helper fails to delete, the checkpoint is left as it wasand the helper's error is returned. Concurrent requests for the same checkpoint mayboth ask for the delete; whichever marks it deprecated first wins, the other gets 404.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[str]
        """
        request_info = self.to_patch_request_information(
            request_configuration
        )
        from .....models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": HttpError,
            "404": HttpError,
            "409": HttpError,
            "500": HttpError,
            "502": HttpError,
            "504": HttpError,
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "str", error_mapping)
    
    def to_patch_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Has a helper on the checkpoint's cluster delete its files (chosen as for the filesendpoints: any helper for a remote checkpoint, the node holding it for a local one),then marks the checkpoint deprecated. A checkpoint without a path has no files todelete and is just deprecated. One with files but no cluster to ask (not takenthrough a checkpoint action) is kept, with a 409, rather than deprecated with itsfiles left behind. If the helper fails to delete, the checkpoint is left as it wasand the helper's error is returned. Concurrent requests for the same checkpoint mayboth ask for the delete; whichever marks it deprecated first wins, the other gets 404.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "text/plain;q=0.9")
        return request_info
    
    def with_url(self,raw_url: str) -> DeprecateItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DeprecateItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DeprecateItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class DeprecateItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

