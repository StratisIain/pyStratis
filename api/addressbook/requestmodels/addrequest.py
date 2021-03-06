from pybitcoin import Model
from pybitcoin.types import Address


class AddRequest(Model):
    """A request model for the addressbook/address endpoint.

    Args:
        address (Address): The address to add to the address book.
        label (str): A label for the address.
    """
    address: Address
    label: str
