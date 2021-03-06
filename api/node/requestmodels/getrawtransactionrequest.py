from typing import Optional
from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import uint256


class GetRawTransactionRequest(Model):
    """A request model for the node/getrawtransaction endpoint.

    Args:
        trxid (uint256): The transaction hash.
        verbose (bool, optional): If output should include verbose transaction data. Default=False.
    """
    trxid: uint256
    verbose: Optional[bool] = Field(default=False)
