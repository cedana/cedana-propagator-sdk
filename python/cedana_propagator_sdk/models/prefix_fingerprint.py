from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PrefixFingerprint(AdditionalDataHolder, Parsable):
    """
    One cumulative prefix fingerprint of the request body, in Switchyard'shash space: `tokens` is the estimated token length of the prefix and`hash` its fold, hex-encoded. Opaque here — recorded and intersected,never recomputed.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The hash property
    hash: Optional[str] = None
    # The tokens property
    tokens: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrefixFingerprint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrefixFingerprint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrefixFingerprint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "hash": lambda n : setattr(self, 'hash', n.get_str_value()),
            "tokens": lambda n : setattr(self, 'tokens', n.get_int_value()),
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
        writer.write_str_value("hash", self.hash)
        writer.write_int_value("tokens", self.tokens)
        writer.write_additional_data_value(self.additional_data)
    

