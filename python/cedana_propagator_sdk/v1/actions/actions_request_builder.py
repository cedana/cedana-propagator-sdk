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
    from ...models.action import Action
    from ...models.http_error import HttpError
    from .from_pod.from_pod_request_builder import From_podRequestBuilder
    from .item.actions_item_request_builder import ActionsItemRequestBuilder
    from .upload.upload_request_builder import UploadRequestBuilder

class ActionsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/actions
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ActionsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/actions{?cluster_id*,type*}", path_parameters)
    
    def by_id(self,id: str) -> ActionsItemRequestBuilder:
        """
        Gets an item from the cedana_propagator_sdk.v1.actions.item collection
        param id: Action UUID
        Returns: ActionsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.actions_item_request_builder import ActionsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return ActionsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ActionsRequestBuilderGetQueryParameters]] = None) -> Optional[list[Action]]:
        """
        List actions
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[Action]]
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
        from ...models.action import Action

        return await self.request_adapter.send_collection_async(request_info, Action, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ActionsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        List actions
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> ActionsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ActionsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ActionsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def from_pod(self) -> From_podRequestBuilder:
        """
        The from_pod property
        """
        from .from_pod.from_pod_request_builder import From_podRequestBuilder

        return From_podRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def upload(self) -> UploadRequestBuilder:
        """
        The upload property
        """
        from .upload.upload_request_builder import UploadRequestBuilder

        return UploadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ActionsRequestBuilderGetQueryParameters():
        """
        List actions
        """
        # Only return actions that ran on this cluster
        cluster_id: Optional[str] = None

        type: Optional[str] = None

    
    @dataclass
    class ActionsRequestBuilderGetRequestConfiguration(RequestConfiguration[ActionsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

