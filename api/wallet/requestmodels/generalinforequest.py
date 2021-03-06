from pydantic import Field
from pybitcoin import Model


class GeneralInfoRequest(Model):
    """A request model for the wallet/general-info endpoint.

    Args:
        name (str): The wallet name.
    """
    name: str = Field(alias='Name')
