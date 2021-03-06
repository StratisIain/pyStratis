from typing import Optional
from pydantic import Field, conint
from pybitcoin import Model, TransactionModel


class GetLastBalanceUpdateTransactionModel(Model):
    """A GetLastBalanceUpdateTransactionModel."""
    transaction: Optional[TransactionModel]
    block_height: Optional[conint(ge=0)] = Field(alias='blockHeight')
