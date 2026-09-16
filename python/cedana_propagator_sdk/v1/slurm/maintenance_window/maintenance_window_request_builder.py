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
    from ....models.create_maintenance_window import CreateMaintenanceWindow
    from ....models.http_error import HttpError
    from ....models.slurm_maintenance_window import SlurmMaintenanceWindow
    from .item.maintenance_window_item_request_builder import Maintenance_windowItemRequestBuilder
    from .sync.sync_request_builder import SyncRequestBuilder

class Maintenance_windowRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/slurm/maintenance_window
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new Maintenance_windowRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/slurm/maintenance_window", path_parameters)
    
    def by_id(self,id: str) -> Maintenance_windowItemRequestBuilder:
        """
        Gets an item from the cedana_propagator_sdk.v1.slurm.maintenance_window.item collection
        param id: Unique identifier of the item
        Returns: Maintenance_windowItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.maintenance_window_item_request_builder import Maintenance_windowItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return Maintenance_windowItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[list[SlurmMaintenanceWindow]]:
        """
        Returns all maintenance windows
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[SlurmMaintenanceWindow]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "500": HttpError,
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.slurm_maintenance_window import SlurmMaintenanceWindow

        return await self.request_adapter.send_collection_async(request_info, SlurmMaintenanceWindow, error_mapping)
    
    async def post(self,body: CreateMaintenanceWindow, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[str]:
        """
        Creates a new maintenance window for SLURM clusters
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[str]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": HttpError,
            "500": HttpError,
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "str", error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns all maintenance windows
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: CreateMaintenanceWindow, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new maintenance window for SLURM clusters
        param body: The request body
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
    
    def with_url(self,raw_url: str) -> Maintenance_windowRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: Maintenance_windowRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return Maintenance_windowRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def sync(self) -> SyncRequestBuilder:
        """
        The sync property
        """
        from .sync.sync_request_builder import SyncRequestBuilder

        return SyncRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class Maintenance_windowRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class Maintenance_windowRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

