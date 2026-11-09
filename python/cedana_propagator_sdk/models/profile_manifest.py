from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .profile_manifest_objects import ProfileManifest_objects

@dataclass
class ProfileManifest(AdditionalDataHolder, Parsable):
    """
    The Kubernetes objects that serve a profile.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The checkpoint_name property
    checkpoint_name: Optional[str] = None
    # The namespace property
    namespace: Optional[str] = None
    # Applied in order with server-side apply; replicas 0 keeps them and stops the pods.
    objects: Optional[list[ProfileManifest_objects]] = None
    # The profile_id property
    profile_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProfileManifest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProfileManifest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProfileManifest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .profile_manifest_objects import ProfileManifest_objects

        from .profile_manifest_objects import ProfileManifest_objects

        fields: dict[str, Callable[[Any], None]] = {
            "checkpoint_name": lambda n : setattr(self, 'checkpoint_name', n.get_str_value()),
            "namespace": lambda n : setattr(self, 'namespace', n.get_str_value()),
            "objects": lambda n : setattr(self, 'objects', n.get_collection_of_object_values(ProfileManifest_objects)),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
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
        writer.write_str_value("checkpoint_name", self.checkpoint_name)
        writer.write_str_value("namespace", self.namespace)
        writer.write_collection_of_object_values("objects", self.objects)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_additional_data_value(self.additional_data)
    

