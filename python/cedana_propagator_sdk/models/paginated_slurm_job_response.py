from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .slurm_available_filters import SlurmAvailableFilters
    from .slurm_job import SlurmJob

@dataclass
class PaginatedSlurmJobResponse(AdditionalDataHolder, Parsable):
    """
    One page of SLURM jobs plus the total number of jobs matching the query,so clients can compute page counts without walking every page.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The available_filters property
    available_filters: Optional[SlurmAvailableFilters] = None
    # The jobs property
    jobs: Optional[list[SlurmJob]] = None
    # The total_count property
    total_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PaginatedSlurmJobResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PaginatedSlurmJobResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PaginatedSlurmJobResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .slurm_available_filters import SlurmAvailableFilters
        from .slurm_job import SlurmJob

        from .slurm_available_filters import SlurmAvailableFilters
        from .slurm_job import SlurmJob

        fields: dict[str, Callable[[Any], None]] = {
            "available_filters": lambda n : setattr(self, 'available_filters', n.get_object_value(SlurmAvailableFilters)),
            "jobs": lambda n : setattr(self, 'jobs', n.get_collection_of_object_values(SlurmJob)),
            "total_count": lambda n : setattr(self, 'total_count', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("available_filters", self.available_filters)
        writer.write_collection_of_object_values("jobs", self.jobs)
        writer.write_int_value("total_count", self.total_count)
        writer.write_additional_data_value(self.additional_data)
    

