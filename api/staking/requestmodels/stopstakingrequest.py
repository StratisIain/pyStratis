import json
from pybitcoin import Model


class StopStakingRequest(Model):
    """A request model for the staking/stopstaking endpoint."""
    def json(self, *args, **kwargs):
        return json.dumps(True)
