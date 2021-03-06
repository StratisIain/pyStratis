from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import uint256


class FullySignedTransferRequest(Model):
    """A request model for the federationgateway/transfer/fullysigned endpoint.

    Args:
        deposit_id (uint256): The deposit id hash.
        transaction_id (uint256): The transaction id hash.
    """
    deposit_id: uint256 = Field(alias='depositId')
    transaction_id: uint256 = Field(alias='transactionId')
