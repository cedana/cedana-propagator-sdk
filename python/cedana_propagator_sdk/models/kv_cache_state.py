from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lmcache_state import LmcacheState

@dataclass
class KvCacheState(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Tokens per KV block. Reuse happens in whole blocks, so a prompt shorter than twoof them reports no hits however often it repeats.
    block_size: Optional[int] = None
    # The gpu_blocks property
    gpu_blocks: Optional[int] = None
    # The lmcache property
    lmcache: Optional[LmcacheState] = None
    # Which worker answered, so a caller can tell a restart apart from acounter that merely moved.
    pod_name: Optional[str] = None
    # The prefix_caching property
    prefix_caching: Optional[bool] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # Prompt tokens the engine has looked up, cumulatively.
    queried_tokens: Optional[int] = None
    # Of those, how many skipped prefill because they were already resident.
    reused_tokens: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> KvCacheState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: KvCacheState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return KvCacheState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .lmcache_state import LmcacheState

        from .lmcache_state import LmcacheState

        fields: dict[str, Callable[[Any], None]] = {
            "block_size": lambda n : setattr(self, 'block_size', n.get_int_value()),
            "gpu_blocks": lambda n : setattr(self, 'gpu_blocks', n.get_int_value()),
            "lmcache": lambda n : setattr(self, 'lmcache', n.get_object_value(LmcacheState)),
            "pod_name": lambda n : setattr(self, 'pod_name', n.get_str_value()),
            "prefix_caching": lambda n : setattr(self, 'prefix_caching', n.get_bool_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "queried_tokens": lambda n : setattr(self, 'queried_tokens', n.get_int_value()),
            "reused_tokens": lambda n : setattr(self, 'reused_tokens', n.get_int_value()),
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
        writer.write_str_value("pod_name", self.pod_name)
        writer.write_bool_value("prefix_caching", self.prefix_caching)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_int_value("queried_tokens", self.queried_tokens)
        writer.write_int_value("reused_tokens", self.reused_tokens)
        writer.write_additional_data_value(self.additional_data)
    

