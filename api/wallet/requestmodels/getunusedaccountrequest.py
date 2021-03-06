from pydantic import Field, SecretStr
from pybitcoin import Model


class GetUnusedAccountRequest(Model):
    """A request model for the wallet/account endpoint.

    Args:
        password (str): The wallet password.
        wallet_name (str): The wallet name.
    """
    password: SecretStr
    wallet_name: str = Field(alias='walletName')
