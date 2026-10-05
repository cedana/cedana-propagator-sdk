from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .router_target_lmcache import RouterTargetLmcache

@dataclass
class RouterTargetKv(AdditionalDataHolder, Parsable):
    """
    KV cache facts for one target, so Switchyard can weigh prefix reuse whenit proposes a profile. Everything here is observed off the target's newestworker, not configured: absent means "no worker has reported yet", and arouter must treat that as "no reuse to be had", not as an error.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Tokens per KV block. Reuse happens in whole blocks and the block beingwritten is never reusable, so this is the quantum every reuse estimatemust round down to. 1600 on a hybrid model, 16 on a dense one.
    block_size: Optional[int] = None
    # The gpu_blocks property
    gpu_blocks: Optional[int] = None
    # The lmcache property
    lmcache: Optional[RouterTargetLmcache] = None
    # The prefix_caching property
    prefix_caching: Optional[bool] = None
    # Prompts shorter than this can never register a hit, however often theyrepeat: two whole blocks (the resident one plus the one being written).
    reuse_floor_tokens: Optional[int] = None
    # How the newest worker pod started: "restore" (its KV cache came backwith it) or "cold" (any prefix knowledge about this profile predatingthe pod is stale). Absent when no worker pod is visible.
    start_kind: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RouterTargetKv:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RouterTargetKv
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RouterTargetKv()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .router_target_lmcache import RouterTargetLmcache

        from .router_target_lmcache import RouterTargetLmcache

        fields: dict[str, Callable[[Any], None]] = {
            "block_size": lambda n : setattr(self, 'block_size', n.get_int_value()),
            "gpu_blocks": lambda n : setattr(self, 'gpu_blocks', n.get_int_value()),
            "lmcache": lambda n : setattr(self, 'lmcache', n.get_object_value(RouterTargetLmcache)),
            "prefix_caching": lambda n : setattr(self, 'prefix_caching', n.get_bool_value()),
            "reuse_floor_tokens": lambda n : setattr(self, 'reuse_floor_tokens', n.get_int_value()),
            "start_kind": lambda n : setattr(self, 'start_kind', n.get_str_value()),
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
        writer.write_int_value("block_size", self.block_size)
        writer.write_int_value("gpu_blocks", self.gpu_blocks)
        writer.write_object_value("lmcache", self.lmcache)
        writer.write_bool_value("prefix_caching", self.prefix_caching)
        writer.write_int_value("reuse_floor_tokens", self.reuse_floor_tokens)
        writer.write_str_value("start_kind", self.start_kind)
        writer.write_additional_data_value(self.additional_data)
    

