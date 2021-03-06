from typing import Optional
from pydantic import Field, conint
from pybitcoin import Model
from pybitcoin.types import uint256


class GetTxOutRequest(Model):
    """A request model for the node/gettxout endpoint.
    Args:
        trxid (uint256): The trxid to check.
        vout (conint(ge=0)): The vout.
        include_mempool (bool, optional): Include mempool in check. Default=True.
    """
    trxid: uint256
    vout: conint(ge=0) = Field(default=0)
    include_mempool: Optional[bool] = Field(default=True, alias='includeMemPool')
