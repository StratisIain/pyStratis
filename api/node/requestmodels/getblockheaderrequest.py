from typing import Optional
from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import uint256


class GetBlockHeaderRequest(Model):
    """A request model for the node/getblockheader endpoint.

    Args:
        block_hash (uint256): The specified block hash.
        is_json_format (bool, optional): If block header should be returned as json. Default=True.
    """
    block_hash: uint256 = Field(alias='hash')
    is_json_format: Optional[bool] = Field(default=True, alias='isJsonFormat')
