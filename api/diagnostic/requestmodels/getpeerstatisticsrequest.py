from pydantic import Field
from pybitcoin import Model


class GetPeerStatisticsRequest(Model):
    """A request model for the diagnostic/getpeerstatistics endpoint.

     Args:
         connected_only (bool): To show data for only connected nodes.
     """
    connected_only: bool = Field(alias='connectedOnly')
