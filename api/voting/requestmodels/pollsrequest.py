from typing import Optional
from pydantic import Field, validator
from pybitcoin import Model, PubKey
from .votekey import VoteKey


class PollsRequest(Model):
    """A request model for multiple voting endpoints.

    Args:
        vote_type (VoteKey, optional): The type of vote to query.
        pubkey_of_member_being_voted_on (PubKey, optional): The pubkey to query.
    """
    vote_type: Optional[VoteKey] = Field(alias='voteType')
    pubkey_of_member_being_voted_on: Optional[PubKey] = Field(alias='pubKeyOfMemberBeingVotedOn')

    # noinspection PyMethodParameters
    @validator('pubkey_of_member_being_voted_on', always=True)
    def check_both_not_none(cls, v, values):
        if v is None and values['vote_type'] is None:
            raise ValueError('Both vote_type and pubkey_of_member_being_voted_on cannot be None.')
        return v
