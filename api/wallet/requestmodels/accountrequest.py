from typing import Optional
from pydantic import Field
from pybitcoin import Model


class AccountRequest(Model):
    """A request model for several wallet endpoints.

    Args:
        wallet_name (str): The wallet name.
        account_name (str, optional): The account name. Default='account 0'.
    """
    wallet_name: str = Field(alias='WalletName')
    account_name: Optional[str] = Field(default='account 0', alias='AccountName')
