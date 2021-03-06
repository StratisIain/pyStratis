from pydantic import Field
from pybitcoin import Model


class DisconnectPeerRequest(Model):
    """A request model for the network/disconnect endpoint.

    Args:
        peer_address (str): The peer endpoint.
    """
    peer_address: str = Field(alias='peerAddress')
