from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activation_forecast import ActivationForecast

@dataclass
class RouteStatusView(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The activation_forecast property
    activation_forecast: Optional[ActivationForecast] = None
    # The endpoint property
    endpoint: Optional[str] = None
    # The fallback_profile_id property
    fallback_profile_id: Optional[str] = None
    # The fallback_ready property
    fallback_ready: Optional[bool] = None
    # The logical_model property
    logical_model: Optional[str] = None
    # A Pending intent asks for this profile to be Active on at least one replica, sosomething is trying to bring it up.
    pending_activation: Optional[bool] = None
    # Any capacity intent for the primary is still Pending, either direction. Rarely thefield you want; prefer pending_activation or pending_release.
    pending_intent: Optional[bool] = None
    # A Pending intent asks for this profile to stop holding an accelerator(Suspended, or Active at zero replicas).
    pending_release: Optional[bool] = None
    # The primary_phase property
    primary_phase: Optional[str] = None
    # The primary_profile_id property
    primary_profile_id: Optional[str] = None
    # The primary_ready property
    primary_ready: Optional[bool] = None
    # The queue_timeout_ms property
    queue_timeout_ms: Optional[int] = None
    # The checkpoint the live worker was told to restore from, when it was.
    restore_checkpoint_path: Optional[str] = None
    # How the worker now on this profile started, read from the pod spec: restore when itwas given a checkpoint, cold otherwise.
    start_kind: Optional[str] = None
    # The state property
    state: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RouteStatusView:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RouteStatusView
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RouteStatusView()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .activation_forecast import ActivationForecast

        from .activation_forecast import ActivationForecast

        fields: dict[str, Callable[[Any], None]] = {
            "activation_forecast": lambda n : setattr(self, 'activation_forecast', n.get_object_value(ActivationForecast)),
            "endpoint": lambda n : setattr(self, 'endpoint', n.get_str_value()),
            "fallback_profile_id": lambda n : setattr(self, 'fallback_profile_id', n.get_str_value()),
            "fallback_ready": lambda n : setattr(self, 'fallback_ready', n.get_bool_value()),
            "logical_model": lambda n : setattr(self, 'logical_model', n.get_str_value()),
            "pending_activation": lambda n : setattr(self, 'pending_activation', n.get_bool_value()),
            "pending_intent": lambda n : setattr(self, 'pending_intent', n.get_bool_value()),
            "pending_release": lambda n : setattr(self, 'pending_release', n.get_bool_value()),
            "primary_phase": lambda n : setattr(self, 'primary_phase', n.get_str_value()),
            "primary_profile_id": lambda n : setattr(self, 'primary_profile_id', n.get_str_value()),
            "primary_ready": lambda n : setattr(self, 'primary_ready', n.get_bool_value()),
            "queue_timeout_ms": lambda n : setattr(self, 'queue_timeout_ms', n.get_int_value()),
            "restore_checkpoint_path": lambda n : setattr(self, 'restore_checkpoint_path', n.get_str_value()),
            "start_kind": lambda n : setattr(self, 'start_kind', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
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
        writer.write_object_value("activation_forecast", self.activation_forecast)
        writer.write_str_value("endpoint", self.endpoint)
        writer.write_str_value("fallback_profile_id", self.fallback_profile_id)
        writer.write_bool_value("fallback_ready", self.fallback_ready)
        writer.write_str_value("logical_model", self.logical_model)
        writer.write_bool_value("pending_activation", self.pending_activation)
        writer.write_bool_value("pending_intent", self.pending_intent)
        writer.write_bool_value("pending_release", self.pending_release)
        writer.write_str_value("primary_phase", self.primary_phase)
        writer.write_str_value("primary_profile_id", self.primary_profile_id)
        writer.write_bool_value("primary_ready", self.primary_ready)
        writer.write_int_value("queue_timeout_ms", self.queue_timeout_ms)
        writer.write_str_value("restore_checkpoint_path", self.restore_checkpoint_path)
        writer.write_str_value("start_kind", self.start_kind)
        writer.write_str_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

