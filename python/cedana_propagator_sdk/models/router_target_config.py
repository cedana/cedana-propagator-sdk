from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .router_target_kv import RouterTargetKv

@dataclass
class RouterTargetConfig(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The current_replicas property
    current_replicas: Optional[int] = None
    # The draining property
    draining: Optional[bool] = None
    # The kv property
    kv: Optional[RouterTargetKv] = None
    # The max_queue_depth property
    max_queue_depth: Optional[int] = None
    # The max_replicas property
    max_replicas: Optional[int] = None
    # The min_replicas property
    min_replicas: Optional[int] = None
    # The node_hourly_usd property
    node_hourly_usd: Optional[float] = None
    # The priority property
    priority: Optional[int] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # The ready property
    ready: Optional[bool] = None
    # Stable internal service URL; never contains an activation/generation.
    service_url: Optional[str] = None
    # The target_concurrency property
    target_concurrency: Optional[int] = None
    # The tier property
    tier: Optional[str] = None
    # The upstream_model property
    upstream_model: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RouterTargetConfig:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RouterTargetConfig
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RouterTargetConfig()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .router_target_kv import RouterTargetKv

        from .router_target_kv import RouterTargetKv

        fields: dict[str, Callable[[Any], None]] = {
            "current_replicas": lambda n : setattr(self, 'current_replicas', n.get_int_value()),
            "draining": lambda n : setattr(self, 'draining', n.get_bool_value()),
            "kv": lambda n : setattr(self, 'kv', n.get_object_value(RouterTargetKv)),
            "max_queue_depth": lambda n : setattr(self, 'max_queue_depth', n.get_int_value()),
            "max_replicas": lambda n : setattr(self, 'max_replicas', n.get_int_value()),
            "min_replicas": lambda n : setattr(self, 'min_replicas', n.get_int_value()),
            "node_hourly_usd": lambda n : setattr(self, 'node_hourly_usd', n.get_float_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "ready": lambda n : setattr(self, 'ready', n.get_bool_value()),
            "service_url": lambda n : setattr(self, 'service_url', n.get_str_value()),
            "target_concurrency": lambda n : setattr(self, 'target_concurrency', n.get_int_value()),
            "tier": lambda n : setattr(self, 'tier', n.get_str_value()),
            "upstream_model": lambda n : setattr(self, 'upstream_model', n.get_str_value()),
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
        writer.write_int_value("current_replicas", self.current_replicas)
        writer.write_bool_value("draining", self.draining)
        writer.write_object_value("kv", self.kv)
        writer.write_int_value("max_queue_depth", self.max_queue_depth)
        writer.write_int_value("max_replicas", self.max_replicas)
        writer.write_int_value("min_replicas", self.min_replicas)
        writer.write_float_value("node_hourly_usd", self.node_hourly_usd)
        writer.write_int_value("priority", self.priority)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_bool_value("ready", self.ready)
        writer.write_str_value("service_url", self.service_url)
        writer.write_int_value("target_concurrency", self.target_concurrency)
        writer.write_str_value("tier", self.tier)
        writer.write_str_value("upstream_model", self.upstream_model)
        writer.write_additional_data_value(self.additional_data)
    

