import json
from pybitcoin import Model


class StopMiningRequest(Model):
    """A request model for the mining/stopmining endpoint."""
    def json(self, *args, **kwargs):
        return json.dumps(True)
