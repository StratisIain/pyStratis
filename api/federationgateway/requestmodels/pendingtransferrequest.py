from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import uint256


class PendingTransferRequest(Model):
    """A request model for the federationgateway/transfer/pending endpoints.

    Args:
        deposit_id (uint256): The deposit id hash.
        transaction_id (uint256): The transaction id hash.
    """
    deposit_id: uint256 = Field(alias='depositId')
    transaction_id: uint256 = Field(alias='transactionId')
