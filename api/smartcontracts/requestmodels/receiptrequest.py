from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import uint256


class ReceiptRequest(Model):
    """A request model for the smartcontracts/receipt endpoint.

    Args:
        tx_hash (uint256): The transaction hash of the smart contract receipt.
    """
    tx_hash: uint256 = Field(alias='txHash')
