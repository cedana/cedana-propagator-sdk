from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activations.activations_request_builder import ActivationsRequestBuilder
    from .analytics.analytics_request_builder import AnalyticsRequestBuilder
    from .artifacts.artifacts_request_builder import ArtifactsRequestBuilder
    from .capacity_intents.capacity_intents_request_builder import CapacityIntentsRequestBuilder
    from .chat.chat_request_builder import ChatRequestBuilder
    from .correlation.correlation_request_builder import CorrelationRequestBuilder
    from .costs.costs_request_builder import CostsRequestBuilder
    from .experiments.experiments_request_builder import ExperimentsRequestBuilder
    from .fleets.fleets_request_builder import FleetsRequestBuilder
    from .history.history_request_builder import HistoryRequestBuilder
    from .keys.keys_request_builder import KeysRequestBuilder
    from .lifecycle_events.lifecycle_events_request_builder import LifecycleEventsRequestBuilder
    from .metrics.metrics_request_builder import MetricsRequestBuilder
    from .models_requests.models_request_builder import ModelsRequestBuilder
    from .observations.observations_request_builder import ObservationsRequestBuilder
    from .outbox.outbox_request_builder import OutboxRequestBuilder
    from .placement.placement_request_builder import PlacementRequestBuilder
    from .profiles.profiles_request_builder import ProfilesRequestBuilder
    from .retention_policies.retention_policies_request_builder import RetentionPoliciesRequestBuilder
    from .router.router_request_builder import RouterRequestBuilder
    from .routes.routes_request_builder import RoutesRequestBuilder
    from .startup_comparison.startup_comparison_request_builder import StartupComparisonRequestBuilder
    from .storage.storage_request_builder import StorageRequestBuilder
    from .usage.usage_request_builder import UsageRequestBuilder
    from .utilization.utilization_request_builder import UtilizationRequestBuilder

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
    def activations(self) -> ActivationsRequestBuilder:
        """
        The activations property
        """
        from .activations.activations_request_builder import ActivationsRequestBuilder

        return ActivationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def analytics(self) -> AnalyticsRequestBuilder:
        """
        The analytics property
        """
        from .analytics.analytics_request_builder import AnalyticsRequestBuilder

        return AnalyticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def artifacts(self) -> ArtifactsRequestBuilder:
        """
        The artifacts property
        """
        from .artifacts.artifacts_request_builder import ArtifactsRequestBuilder

        return ArtifactsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def capacity_intents(self) -> CapacityIntentsRequestBuilder:
        """
        The capacityIntents property
        """
        from .capacity_intents.capacity_intents_request_builder import CapacityIntentsRequestBuilder

        return CapacityIntentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def chat(self) -> ChatRequestBuilder:
        """
        The chat property
        """
        from .chat.chat_request_builder import ChatRequestBuilder

        return ChatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def correlation(self) -> CorrelationRequestBuilder:
        """
        The correlation property
        """
        from .correlation.correlation_request_builder import CorrelationRequestBuilder

        return CorrelationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def costs(self) -> CostsRequestBuilder:
        """
        The costs property
        """
        from .costs.costs_request_builder import CostsRequestBuilder

        return CostsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def experiments(self) -> ExperimentsRequestBuilder:
        """
        The experiments property
        """
        from .experiments.experiments_request_builder import ExperimentsRequestBuilder

        return ExperimentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fleets(self) -> FleetsRequestBuilder:
        """
        The fleets property
        """
        from .fleets.fleets_request_builder import FleetsRequestBuilder

        return FleetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def history(self) -> HistoryRequestBuilder:
        """
        The history property
        """
        from .history.history_request_builder import HistoryRequestBuilder

        return HistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    def observations(self) -> ObservationsRequestBuilder:
        """
        The observations property
        """
        from .observations.observations_request_builder import ObservationsRequestBuilder

        return ObservationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def outbox(self) -> OutboxRequestBuilder:
        """
        The outbox property
        """
        from .outbox.outbox_request_builder import OutboxRequestBuilder

        return OutboxRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def placement(self) -> PlacementRequestBuilder:
        """
        The placement property
        """
        from .placement.placement_request_builder import PlacementRequestBuilder

        return PlacementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def profiles(self) -> ProfilesRequestBuilder:
        """
        The profiles property
        """
        from .profiles.profiles_request_builder import ProfilesRequestBuilder

        return ProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def retention_policies(self) -> RetentionPoliciesRequestBuilder:
        """
        The retentionPolicies property
        """
        from .retention_policies.retention_policies_request_builder import RetentionPoliciesRequestBuilder

        return RetentionPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def router(self) -> RouterRequestBuilder:
        """
        The router property
        """
        from .router.router_request_builder import RouterRequestBuilder

        return RouterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def routes(self) -> RoutesRequestBuilder:
        """
        The routes property
        """
        from .routes.routes_request_builder import RoutesRequestBuilder

        return RoutesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def startup_comparison(self) -> StartupComparisonRequestBuilder:
        """
        The startupComparison property
        """
        from .startup_comparison.startup_comparison_request_builder import StartupComparisonRequestBuilder

        return StartupComparisonRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def storage(self) -> StorageRequestBuilder:
        """
        The storage property
        """
        from .storage.storage_request_builder import StorageRequestBuilder

        return StorageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def usage(self) -> UsageRequestBuilder:
        """
        The usage property
        """
        from .usage.usage_request_builder import UsageRequestBuilder

        return UsageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def utilization(self) -> UtilizationRequestBuilder:
        """
        The utilization property
        """
        from .utilization.utilization_request_builder import UtilizationRequestBuilder

        return UtilizationRequestBuilder(self.request_adapter, self.path_parameters)
    

