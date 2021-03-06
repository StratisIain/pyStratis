from pydantic import Field
from pybitcoin import Model


class GetAccountsRequest(Model):
    """A request model for the wallet/accounts endpoint.

    Args:
        wallet_name (str): The wallet name.
    """
    wallet_name: str = Field(alias='WalletName')
