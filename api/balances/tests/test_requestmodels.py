import json
from api.balances.requestmodels import *
from pybitcoin.types import Money


def test_overamountatheightrequest():
    data = {
        'blockHeight': 1,
        'amount': '5.00000000'
    }
    request_model = OverAmountAtHeightRequest(
        block_height=1,
        amount=Money(5)
    )
    assert json.dumps(data) == request_model.json()
