from pydantic import Field
from pybitcoin import Model
from pybitcoin.types import uint256


class SyncRequest(Model):
    """A request_model for the notifications/sync endpoint.

    Args:
        sync_from (uint256): The block hash to start syncing at.
    """
    sync_from: uint256 = Field(alias='from')
