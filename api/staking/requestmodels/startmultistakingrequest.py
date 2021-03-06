from typing import List
from pydantic import Field
from pybitcoin import Model, WalletSecret


class StartMultiStakingRequest(Model):
    """A request model for the staking/startmultistaking endpoint.

    Args:
        wallet_credentials (List[WalletSecret]): A list of wallet credentials to launch staking of multiple wallets with one command.
    """
    wallet_credentials: List[WalletSecret] = Field(alias='walletCredentials')
