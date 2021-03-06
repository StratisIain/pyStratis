from pydantic import Field
from pybitcoin import Model


class GetUTXOSetRequest(Model):
    """A request model for the GetUTXOSetRequest.

    Args:
        at_block_height (int): The specified block height.
    """
    at_block_height: int = Field(alias='atBlockHeight')
