from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorize.authorize_request_builder import AuthorizeRequestBuilder
    from .config.config_request_builder import ConfigRequestBuilder
    from .lifetime.lifetime_request_builder import LifetimeRequestBuilder
    from .metrics.metrics_request_builder import MetricsRequestBuilder
    from .resolve.resolve_request_builder import ResolveRequestBuilder
    from .telemetry.telemetry_request_builder import TelemetryRequestBuilder

class RouterRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/inference/router
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new RouterRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/inference/router", path_parameters)
    
    @property
    def authorize(self) -> AuthorizeRequestBuilder:
        """
        The authorize property
        """
        from .authorize.authorize_request_builder import AuthorizeRequestBuilder

        return AuthorizeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def config(self) -> ConfigRequestBuilder:
        """
        The config property
        """
        from .config.config_request_builder import ConfigRequestBuilder

        return ConfigRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def lifetime(self) -> LifetimeRequestBuilder:
        """
        The lifetime property
        """
        from .lifetime.lifetime_request_builder import LifetimeRequestBuilder

        return LifetimeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def metrics(self) -> MetricsRequestBuilder:
        """
        The metrics property
        """
        from .metrics.metrics_request_builder import MetricsRequestBuilder

        return MetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resolve(self) -> ResolveRequestBuilder:
        """
        The resolve property
        """
        from .resolve.resolve_request_builder import ResolveRequestBuilder

        return ResolveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def telemetry(self) -> TelemetryRequestBuilder:
        """
        The telemetry property
        """
        from .telemetry.telemetry_request_builder import TelemetryRequestBuilder

        return TelemetryRequestBuilder(self.request_adapter, self.path_parameters)
    

