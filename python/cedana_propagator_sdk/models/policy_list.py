from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .policy import Policy
    from .scoped_policy import ScopedPolicy

@dataclass
class PolicyList(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A policy at one scope; an absent field inherits from the next scope.
    org: Optional[Policy] = None
    # The profiles property
    profiles: Optional[list[ScopedPolicy]] = None
    # Every team named on a profile or a policy.
    team_names: Optional[list[str]] = None
    # The teams property
    teams: Optional[list[ScopedPolicy]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyList:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyList
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PolicyList()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .policy import Policy
        from .scoped_policy import ScopedPolicy

        from .policy import Policy
        from .scoped_policy import ScopedPolicy

        fields: dict[str, Callable[[Any], None]] = {
            "org": lambda n : setattr(self, 'org', n.get_object_value(Policy)),
            "profiles": lambda n : setattr(self, 'profiles', n.get_collection_of_object_values(ScopedPolicy)),
            "team_names": lambda n : setattr(self, 'team_names', n.get_collection_of_primitive_values(str)),
            "teams": lambda n : setattr(self, 'teams', n.get_collection_of_object_values(ScopedPolicy)),
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
        writer.write_object_value("org", self.org)
        writer.write_collection_of_object_values("profiles", self.profiles)
        writer.write_collection_of_primitive_values("team_names", self.team_names)
        writer.write_collection_of_object_values("teams", self.teams)
        writer.write_additional_data_value(self.additional_data)
    

