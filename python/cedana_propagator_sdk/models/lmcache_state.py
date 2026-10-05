from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LmcacheState(AdditionalDataHolder, Parsable):
    """
    What a profile's engine is currently reusing.LMCache counters for one worker, as `lmcache server` exports them on itsPrometheus port (`--prometheus-port`, 9090 by default). Every field isoptional: the propagator stores what the controller scraped and neverinvents a tier that did not report.Tiers: L1 is pinned CPU DRAM inside the `lmcache server` process, L2 thenode's local NVMe behind the POSIX `nixl_store` adapter. Unlike KVBM'stiers these live **outside** the vLLM worker — one server per node, sharedby every pod on it — so `node` records which server produced the numbers,and two workers on the same node necessarily report the same ones.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Tokens served from the cache rather than prefilled — LMCache'sequivalent of what KVBM called `matched_tokens`.
    hit_tokens: Optional[int] = None
    # The l1_capacity_bytes property
    l1_capacity_bytes: Optional[int] = None
    # 0.0–1.0. Derived, not reported: the server exports per-tier hit TOKENSagainst one shared denominator, never a rate.
    l1_hit_rate: Optional[float] = None
    # The l1_used_bytes property
    l1_used_bytes: Optional[int] = None
    # The l2_capacity_bytes property
    l2_capacity_bytes: Optional[int] = None
    # The l2_hit_rate property
    l2_hit_rate: Optional[float] = None
    # The l2_used_bytes property
    l2_used_bytes: Optional[int] = None
    # The load_chunks property
    load_chunks: Optional[int] = None
    # The node whose `lmcache server` produced these counters. The cache isper-node, so this, not the pod, is the identity that matters.
    node: Optional[str] = None
    # Tokens looked up, hit or miss. With `hit_tokens` this gives a ratethat does not depend on the server exporting one.
    requested_tokens: Optional[int] = None
    # Chunks written into the cache, and read back out of it.
    store_chunks: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LmcacheState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LmcacheState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LmcacheState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "hit_tokens": lambda n : setattr(self, 'hit_tokens', n.get_int_value()),
            "l1_capacity_bytes": lambda n : setattr(self, 'l1_capacity_bytes', n.get_int_value()),
            "l1_hit_rate": lambda n : setattr(self, 'l1_hit_rate', n.get_float_value()),
            "l1_used_bytes": lambda n : setattr(self, 'l1_used_bytes', n.get_int_value()),
            "l2_capacity_bytes": lambda n : setattr(self, 'l2_capacity_bytes', n.get_int_value()),
            "l2_hit_rate": lambda n : setattr(self, 'l2_hit_rate', n.get_float_value()),
            "l2_used_bytes": lambda n : setattr(self, 'l2_used_bytes', n.get_int_value()),
            "load_chunks": lambda n : setattr(self, 'load_chunks', n.get_int_value()),
            "node": lambda n : setattr(self, 'node', n.get_str_value()),
            "requested_tokens": lambda n : setattr(self, 'requested_tokens', n.get_int_value()),
            "store_chunks": lambda n : setattr(self, 'store_chunks', n.get_int_value()),
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
        writer.write_int_value("hit_tokens", self.hit_tokens)
        writer.write_int_value("l1_capacity_bytes", self.l1_capacity_bytes)
        writer.write_float_value("l1_hit_rate", self.l1_hit_rate)
        writer.write_int_value("l1_used_bytes", self.l1_used_bytes)
        writer.write_int_value("l2_capacity_bytes", self.l2_capacity_bytes)
        writer.write_float_value("l2_hit_rate", self.l2_hit_rate)
        writer.write_int_value("l2_used_bytes", self.l2_used_bytes)
        writer.write_int_value("load_chunks", self.load_chunks)
        writer.write_str_value("node", self.node)
        writer.write_int_value("requested_tokens", self.requested_tokens)
        writer.write_int_value("store_chunks", self.store_chunks)
        writer.write_additional_data_value(self.additional_data)
    

