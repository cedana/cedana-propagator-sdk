from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class RouterTargetLmcache(AdditionalDataHolder, Parsable):
    """
    What the router may assume about a target's LMCache tiers: what wasconfigured (from the profile's template) and whether each tier has everheld anything (from the newest worker's counters). The countersthemselves ride along for display; they change on every scrape and aredeliberately not part of the ETag, so read them as approximate.One caveat the KVBM version did not have: the cache is per node, shared byevery pod on it, so these counters describe the node the newest workerlanded on rather than that worker alone. `node` says which.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The hit_rate property
    hit_rate: Optional[float] = None
    # The hit_tokens property
    hit_tokens: Optional[int] = None
    # The l1_active property
    l1_active: Optional[bool] = None
    # The l1_hit_rate property
    l1_hit_rate: Optional[float] = None
    # The l1_size_gb property
    l1_size_gb: Optional[float] = None
    # The l2_active property
    l2_active: Optional[bool] = None
    # The l2_hit_rate property
    l2_hit_rate: Optional[float] = None
    # The l2_size_gb property
    l2_size_gb: Optional[float] = None
    # The node property
    node: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RouterTargetLmcache:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RouterTargetLmcache
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RouterTargetLmcache()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "hit_rate": lambda n : setattr(self, 'hit_rate', n.get_float_value()),
            "hit_tokens": lambda n : setattr(self, 'hit_tokens', n.get_int_value()),
            "l1_active": lambda n : setattr(self, 'l1_active', n.get_bool_value()),
            "l1_hit_rate": lambda n : setattr(self, 'l1_hit_rate', n.get_float_value()),
            "l1_size_gb": lambda n : setattr(self, 'l1_size_gb', n.get_float_value()),
            "l2_active": lambda n : setattr(self, 'l2_active', n.get_bool_value()),
            "l2_hit_rate": lambda n : setattr(self, 'l2_hit_rate', n.get_float_value()),
            "l2_size_gb": lambda n : setattr(self, 'l2_size_gb', n.get_float_value()),
            "node": lambda n : setattr(self, 'node', n.get_str_value()),
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
        writer.write_float_value("hit_rate", self.hit_rate)
        writer.write_int_value("hit_tokens", self.hit_tokens)
        writer.write_bool_value("l1_active", self.l1_active)
        writer.write_float_value("l1_hit_rate", self.l1_hit_rate)
        writer.write_float_value("l1_size_gb", self.l1_size_gb)
        writer.write_bool_value("l2_active", self.l2_active)
        writer.write_float_value("l2_hit_rate", self.l2_hit_rate)
        writer.write_float_value("l2_size_gb", self.l2_size_gb)
        writer.write_str_value("node", self.node)
        writer.write_additional_data_value(self.additional_data)
    

