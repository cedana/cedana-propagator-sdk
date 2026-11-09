from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .deployment_profile import DeploymentProfile

from .deployment_profile import DeploymentProfile

@dataclass
class ProfileView(DeploymentProfile, Parsable):
    """
    A profile with its live state, read from the regular pod sync.
    """
    # The ready_replicas property
    ready_replicas: Optional[int] = None
    # How the newest worker started: "restore" or "cold"; null with no worker.
    start_kind: Optional[str] = None
    # "serving", "starting" or "scaled_to_zero".
    state: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProfileView:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProfileView
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProfileView()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .deployment_profile import DeploymentProfile

        from .deployment_profile import DeploymentProfile

        fields: dict[str, Callable[[Any], None]] = {
            "ready_replicas": lambda n : setattr(self, 'ready_replicas', n.get_int_value()),
            "start_kind": lambda n : setattr(self, 'start_kind', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_int_value("ready_replicas", self.ready_replicas)
        writer.write_str_value("start_kind", self.start_kind)
        writer.write_str_value("state", self.state)
    

