from typing import Union, List
from api import APIRequest, EndpointRegister, endpoint
from api.node.requestmodels import *
from api.node.responsemodels import *
from pybitcoin import ScriptPubKey, LogRule
from pybitcoin.types import Address, hexstr, Money, uint256


class Node(APIRequest, metaclass=EndpointRegister):
    route = '/api/node'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @endpoint(f'{route}/status')
    def status(self, **kwargs) -> StatusModel:
        """Gets the node status.

        Args:
            **kwargs:

        Returns:
            StatusModel

        Raises:
            APIError
        """
        data = self.get(**kwargs)
        return StatusModel(**data)

    @endpoint(f'{route}/getblockheader')
    def get_blockheader(self,
                        block_hash: Union[str, uint256],
                        is_json_format: bool = True,
                        **kwargs) -> BlockHeaderModel:
        """Gets the specified block header.

        Args:
            block_hash (str | uint256): The specified block hash.
            is_json_format (bool, optional): If block header should be returned as json. Default=True.
            **kwargs:

        Returns:
            BlockHeaderModel

        Raises:
            APIError
        """
        if isinstance(block_hash, str):
            block_hash = uint256(block_hash)
        request_model = GetBlockHeaderRequest(block_hash=block_hash, is_json_format=is_json_format)
        data = self.get(request_model, **kwargs)

        return BlockHeaderModel(**data)

    @endpoint(f'{route}/getrawtransaction')
    def get_raw_transaction(self,
                            trxid: Union[uint256, str],
                            verbose: bool = False,
                            **kwargs) -> Union[hexstr, TransactionModel]:
        """Gets a raw transaction from a transaction id.

        Args:
            trxid (uint256 | str): The transaction hash.
            verbose (bool, optional): If output should include verbose transaction data. Default=False.
            **kwargs:

        Returns:
            Union[hexstr, TransactionModel]

        Raises:
            APIError
        """
        if isinstance(trxid, str):
            trxid = uint256(trxid)
        request_model = GetRawTransactionRequest(trxid=trxid, verbose=verbose)
        data = self.get(request_model, **kwargs)
        if data is None:
            raise RuntimeWarning('Transaction not found. Is -txindex=1 enabled?')
        if not request_model.verbose:
            return hexstr(data)
        return TransactionModel(**data)

    @endpoint(f'{route}/decoderawtransaction')
    def decode_raw_transaction(self, raw_hex: Union[str, hexstr], **kwargs) -> TransactionModel:
        """Decodes raw transaction hex into a transaction model.

        Args:
            raw_hex (hexstr | str): The transaction hexstring.
            **kwargs:

        Returns:
            TransactionModel

        Raises:
            APIError
        """
        if isinstance(raw_hex, str):
            raw_hex = hexstr(raw_hex)
        request_model = DecodeRawTransactionRequest(raw_hex=raw_hex)
        data = self.post(request_model, **kwargs)
        return TransactionModel(**data)

    @endpoint(f'{route}/validateaddress')
    def validate_address(self, address: str, **kwargs) -> ValidateAddressModel:
        """Validate an address

        Args:
            address (str): The address to validate.
            **kwargs:

        Returns:
            ValidateAddressModel

        Raises:
            APIError
        """
        request_model = ValidateAddressRequest(address=address)
        data = self.get(request_model, **kwargs)
        data['address'] = Address(address=data['address'], network=self._network)
        return ValidateAddressModel(**data)

    @endpoint(f'{route}/gettxout')
    def get_txout(self,
                  trxid: Union[uint256, str],
                  vout: int,
                  include_mempool: bool = True,
                  **kwargs) -> GetTxOutModel:
        """Gets a specified txout from a given transaction.

        Args:
            trxid (uint256 | str): The trxid to check.
            vout (int): The vout.
            include_mempool (bool, optional): Include mempool in check. Default=True.
            **kwargs:

        Returns:
            GetTxOutModel

        Raises:
            APIError
        """
        if isinstance(trxid, str):
            trxid = uint256(trxid)
        request_model = GetTxOutRequest(trxid=trxid, vout=vout, include_mempool=include_mempool)
        data = self.get(request_model, **kwargs)
        if data is not None:
            if 'value' in data:
                data['value'] = Money.from_satoshi_units(data['value'])
            if 'scriptPubKey' in data:
                data['scriptPubKey'] = ScriptPubKey(**data['scriptPubKey'])
            return GetTxOutModel(**data)

    @endpoint(f'{route}/gettxoutproof')
    def get_txout_proof(self,
                        txids: List[Union[str, uint256]],
                        block_hash: Union[uint256, str],
                        **kwargs) -> hexstr:
        """The merkle proof that the specified transaction exist in a given block.

        Should have txindex enabled if not specifying blockhash.

        Args:
            txids (List[uint256]): A list of transaction hashes.
            block_hash (uint256, optional): The block hash to check.
            **kwargs:

        Returns:
            hexstr

        Raises:
            APIError
        """
        for i in range(len(txids)):
            if isinstance(txids[i], str):
                txids[i] = uint256(txids[i])
        if isinstance(block_hash, str):
            block_hash = uint256(block_hash)
        request_model = GetTxOutProofRequest(txids=txids, block_hash=block_hash)
        data = self.get(request_model, **kwargs)
        return hexstr(data)

    @endpoint(f'{route}/shutdown')
    def shutdown(self, **kwargs) -> None:
        """Triggers node shutdown.

        Args:
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
        request_model = ShutdownRequest()
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/stop')
    def stop(self, **kwargs) -> None:
        """Triggers node shutdown.

        Args:
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
        request_model = ShutdownRequest()
        self.post(request_model, **kwargs)

    @endpoint(f'{route}/loglevels')
    def log_levels(self, log_rules: List[LogRule], **kwargs) -> None:
        """Changes log level for the specified loggers.

        Args:
            log_rules (List[LogRule]): A list of log rules to change.
            **kwargs:

        Returns:
            None

        Raises:
            APIError
        """
        request_model = LogRulesRequest(log_rules=log_rules)
        self.put(request_model, **kwargs)

    @endpoint(f'{route}/logrules')
    def log_rules(self, **kwargs) -> List[LogRulesModel]:
        """Returns the enabled log rules.

        Args:
            **kwargs:

        Returns:
            List[LogRulesModel]

        Raises:
            APIError

        """
        data = self.get(**kwargs)
        return [LogRulesModel(**x) for x in data]

    @endpoint(f'{route}/asyncloops')
    def async_loops(self, **kwargs) -> List[AsyncLoopsModel]:
        """Gets the currently running async loops.

        Args:
            **kwargs:

        Returns:
            List[AsyncLoopsModel]

        Raises:
            APIError
        """
        data = self.get(**kwargs)
        return [AsyncLoopsModel(**x) for x in data]
