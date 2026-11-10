from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alerts.alerts_request_builder import AlertsRequestBuilder
    from .costs.costs_request_builder import CostsRequestBuilder
    from .events.events_request_builder import EventsRequestBuilder
    from .gateways.gateways_request_builder import GatewaysRequestBuilder
    from .keys.keys_request_builder import KeysRequestBuilder
    from .lifecycle_events.lifecycle_events_request_builder import LifecycleEventsRequestBuilder
    from .metrics.metrics_request_builder import MetricsRequestBuilder
    from .models_requests.models_request_builder import ModelsRequestBuilder
    from .profiles.profiles_request_builder import ProfilesRequestBuilder
    from .router.router_request_builder import RouterRequestBuilder
    from .slo.slo_request_builder import SloRequestBuilder
    from .startup_comparison.startup_comparison_request_builder import StartupComparisonRequestBuilder
    from .usage.usage_request_builder import UsageRequestBuilder

class InferenceRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/inference
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new InferenceRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/inference", path_parameters)
    
    @property
    def alerts(self) -> AlertsRequestBuilder:
        """
        The alerts property
        """
        from .alerts.alerts_request_builder import AlertsRequestBuilder

        return AlertsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def costs(self) -> CostsRequestBuilder:
        """
        The costs property
        """
        from .costs.costs_request_builder import CostsRequestBuilder

        return CostsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def events(self) -> EventsRequestBuilder:
        """
        The events property
        """
        from .events.events_request_builder import EventsRequestBuilder

        return EventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gateways(self) -> GatewaysRequestBuilder:
        """
        The gateways property
        """
        from .gateways.gateways_request_builder import GatewaysRequestBuilder

        return GatewaysRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def keys(self) -> KeysRequestBuilder:
        """
        The keys property
        """
        from .keys.keys_request_builder import KeysRequestBuilder

        return KeysRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def lifecycle_events(self) -> LifecycleEventsRequestBuilder:
        """
        The lifecycleEvents property
        """
        from .lifecycle_events.lifecycle_events_request_builder import LifecycleEventsRequestBuilder

        return LifecycleEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def metrics(self) -> MetricsRequestBuilder:
        """
        The metrics property
        """
        from .metrics.metrics_request_builder import MetricsRequestBuilder

        return MetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def models(self) -> ModelsRequestBuilder:
        """
        The models property
        """
        from .models_requests.models_request_builder import ModelsRequestBuilder

        return ModelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def profiles(self) -> ProfilesRequestBuilder:
        """
        The profiles property
        """
        from .profiles.profiles_request_builder import ProfilesRequestBuilder

        return ProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def router(self) -> RouterRequestBuilder:
        """
        The router property
        """
        from .router.router_request_builder import RouterRequestBuilder

        return RouterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def slo(self) -> SloRequestBuilder:
        """
        The slo property
        """
        from .slo.slo_request_builder import SloRequestBuilder

        return SloRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def startup_comparison(self) -> StartupComparisonRequestBuilder:
        """
        The startupComparison property
        """
        from .startup_comparison.startup_comparison_request_builder import StartupComparisonRequestBuilder

        return StartupComparisonRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def usage(self) -> UsageRequestBuilder:
        """
        The usage property
        """
        from .usage.usage_request_builder import UsageRequestBuilder

        return UsageRequestBuilder(self.request_adapter, self.path_parameters)
    

