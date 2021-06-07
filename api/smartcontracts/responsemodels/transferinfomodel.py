from typing import Optional
from pydantic import Field
from pybitcoin import Model, Address
from pybitcoin.types import Money


class TransferInfoModel(Model):
    """A TransferInfoModel."""
    from_address: Optional[Address] = Field(alias='From')
    to_address: Optional[Address] = Field(alias='To')
    value: Optional[Money] = Field(alias='Value')
