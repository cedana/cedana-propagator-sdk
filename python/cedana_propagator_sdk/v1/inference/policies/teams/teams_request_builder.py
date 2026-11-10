from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_team_item_request_builder import WithTeamItemRequestBuilder

class TeamsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/inference/policies/teams
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TeamsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/inference/policies/teams", path_parameters)
    
    def by_team(self,team: str) -> WithTeamItemRequestBuilder:
        """
        Gets an item from the cedana_propagator_sdk.v1.inference.policies.teams.item collection
        param team: Unique identifier of the item
        Returns: WithTeamItemRequestBuilder
        """
        if team is None:
            raise TypeError("team cannot be null.")
        from .item.with_team_item_request_builder import WithTeamItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["team"] = team
        return WithTeamItemRequestBuilder(self.request_adapter, url_tpl_params)
    

