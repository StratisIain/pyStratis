from pydantic import Field
from pybitcoin import Model


class InfoRequest(Model):
    """A request model for the coldstaking/cold-staking-info endpoint.

    Args:
        wallet_name (str): The wallet name.
    """
    wallet_name: str = Field(alias='WalletName')
