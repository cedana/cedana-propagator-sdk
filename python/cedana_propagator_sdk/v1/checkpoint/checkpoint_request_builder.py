from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .checksum.checksum_request_builder import ChecksumRequestBuilder
    from .path.path_request_builder import PathRequestBuilder
    from .pod.pod_request_builder import PodRequestBuilder
    from .status.status_request_builder import StatusRequestBuilder

class CheckpointRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/checkpoint
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CheckpointRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/checkpoint", path_parameters)
    
    @property
    def checksum(self) -> ChecksumRequestBuilder:
        """
        The checksum property
        """
        from .checksum.checksum_request_builder import ChecksumRequestBuilder

        return ChecksumRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def path(self) -> PathRequestBuilder:
        """
        The path property
        """
        from .path.path_request_builder import PathRequestBuilder

        return PathRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pod(self) -> PodRequestBuilder:
        """
        The pod property
        """
        from .pod.pod_request_builder import PodRequestBuilder

        return PodRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def status(self) -> StatusRequestBuilder:
        """
        The status property
        """
        from .status.status_request_builder import StatusRequestBuilder

        return StatusRequestBuilder(self.request_adapter, self.path_parameters)
    

