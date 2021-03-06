from typing import Optional
from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import Address


class ValidateAddressModel(Model):
    """A ValidateAddressModel."""
    isvalid: Optional[bool]
    address: Optional[Address]
    scriptPubKey: Optional[str] = Field(alias='scriptPubKey')
    isscript: Optional[bool]
    iswitness: Optional[bool]
