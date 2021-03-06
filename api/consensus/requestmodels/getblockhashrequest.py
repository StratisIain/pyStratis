from pydantic import conint
from pybitcoin import Model


class GetBlockHashRequest(Model):
    """A request model for the consensus/getblockhash endpoint.

    Args:
        height (conint(ge=0)): The requested height for block hash retrieval.
    """
    height: conint(ge=0)
