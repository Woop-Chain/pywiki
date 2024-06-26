"""
Interact with Woop's transaction RPC API
"""

import time
import random
from .constants import DEFAULT_ENDPOINT, DEFAULT_TIMEOUT
from .rpc.request import rpc_request
from .exceptions import TxConfirmationTimedoutError, InvalidRPCReplyError


#########################
# Transaction Pool RPCs #
#########################
def get_pending_transactions(
    endpoint = DEFAULT_ENDPOINT,
    timeout = DEFAULT_TIMEOUT
) -> list:
    """Get list of pending transactions.

    Parameters
    ----------
    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    list of transactions in the pool, see get_transaction_by_hash for a description

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://api.woopchain.com/#de6c4a12-fa42-44e8-972f-801bfde1dd18
    """
    method = "wikiv2_pendingTransactions"
    try:
        return rpc_request( method,
                            endpoint = endpoint,
                            timeout = timeout )[ "result" ]
    except KeyError as exception:
        raise InvalidRPCReplyError( method, endpoint ) from exception


def get_transaction_error_sink(
    endpoint = DEFAULT_ENDPOINT,
    timeout = DEFAULT_TIMEOUT
) -> list:
    """Get current transactions error sink.

    Parameters
    ----------
    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    list of transaction failure dictionaries with the following keys:
        tx-hash-id: :obj:`str` Transaction hash
        time-at-rejection: :obj:`int` Unix time when the transaction was rejected from the pool
        error-message: :obj:`str` Reason for transaction rejection (for example insufficient funds)

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://api.woopchain.com/#9aedbc22-6262-44b1-8276-cd8ae19fa600
    """
    method = "wikiv2_getCurrentTransactionErrorSink"
    try:
        return rpc_request( method,
                            endpoint = endpoint,
                            timeout = timeout )[ "result" ]
    except KeyError as exception:
        raise InvalidRPCReplyError( method, endpoint ) from exception


def get_pending_staking_transactions(
    endpoint = DEFAULT_ENDPOINT,
    timeout = DEFAULT_TIMEOUT
) -> list:
    """Get list of pending staking transactions.

    Parameters
    ----------
    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    list of staking transactions in the pool, see get_staking_transaction_by_hash for a description

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://api.woopchain.com/#de0235e4-f4c9-4a69-b6d2-b77dc1ba7b12
    """
    method = "wikiv2_pendingStakingTransactions"
    try:
        return rpc_request( method,
                            endpoint = endpoint,
                            timeout = timeout )[ "result" ]
    except KeyError as exception:
        raise InvalidRPCReplyError( method, endpoint ) from exception


def get_staking_transaction_error_sink(
    endpoint = DEFAULT_ENDPOINT,
    timeout = DEFAULT_TIMEOUT
) -> list:
    """Get current staking transactions error sink.

    Parameters
    ----------
    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    list of transaction failure dictionaries with the following keys:
        tx-hash-id: :obj:`str` Transaction hash
        time-at-rejection: :obj:`int` Unix time when the transaction was rejected from the pool
        error-message: :obj:`str` Reason for transaction rejection (for example insufficient funds)
        directive-kind: :obj:`str` Tope of staking transaction

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://api.woopchain.com/#bdd00e0f-2ba0-480e-b996-2ef13f10d75a
    """
    method = "wikiv2_getCurrentStakingErrorSink"
    try:
        return rpc_request( method,
                            endpoint = endpoint,
                            timeout = timeout )[ "result" ]
    except KeyError as exception:
        raise InvalidRPCReplyError( method, endpoint ) from exception


def get_pool_stats(
    endpoint = DEFAULT_ENDPOINT,
    timeout = DEFAULT_TIMEOUT
) -> dict:
    """Get stats of the pool, that is, number of pending and queued (non-
    executable) transactions.

    Parameters
    ----------
    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    dict with the following keys:
        executable-count: :obj:`int` Number of pending transactions
        non-executable-count: :obj:`int` Number of queued (non-executable) transactions

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://api.woopchain.com/#7c2b9395-8f5e-4eb5-a687-2f1be683d83e
    """
    method = "wikiv2_getPoolStats"
    try:
        return rpc_request( method,
                            endpoint = endpoint,
                            timeout = timeout )[ "result" ]
    except KeyError as exception:
        raise InvalidRPCReplyError( method, endpoint ) from exception


####################
# Transaction RPCs #
####################
def get_transaction_by_hash(
    tx_hash,
    endpoint = DEFAULT_ENDPOINT,
    timeout = DEFAULT_TIMEOUT
) -> dict:
    """Get transaction by hash.

    Parameters
    ----------
    tx_hash: str
        Transaction hash to fetch
    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    dict with the following keys
        blockHash: :obj:`str` Block hash that transaction was finalized;
            "0x0000000000000000000000000000000000000000000000000000000000000000" if tx is pending
        blockNumber: :obj:`int` Block number that transaction was finalized; None if tx is pending
        ethHash: :obj:`str` legacy from Ethereum; unused
        from: :obj:`str` Wallet address
        timestamp: :obj:`int` Timestamp in Unix time when transaction was finalized
        gas: :obj:`int` Gas limit in Atto
        gasPrice :obj:`int` Gas price in Atto
        hash: :obj:`str` Transaction hash
        input: :obj:`str` Transaction data, used for smart contracts
        nonce: :obj:`int` Wallet nonce for the transaction
        to: :obj:`str` Wallet address of the receiver
        transactionIndex: :obj:`int` Index of transaction in block; None if tx is pending
        value: :obj:`int` Amount transferred in Atto
        shardID: :obj:`int` Shard where amount if from
        toShardID: :obj:`int` Shard where the amount is sent
        r: :obj:`str` First 32 bytes of the transaction signature
        s: :obj:`str` Next  32 bytes of the transaction signature
        v: :obj:`str` Recovery value + 27, as hex string
    or None if the transaction is not found

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://api.woopchain.com/#117e84f6-a0ec-444e-abe0-455701310389
    """
    method = "wikiv2_getTransactionByHash"
    params = [ tx_hash ]
    try:
        return rpc_request(
            method,
            params = params,
            endpoint = endpoint,
            timeout = timeout
        )[ "result" ]
    except KeyError as exception:
        raise InvalidRPCReplyError( method, endpoint ) from exception


def get_transaction_by_block_hash_and_index(
    block_hash,
    tx_index,
    endpoint = DEFAULT_ENDPOINT,
    timeout = DEFAULT_TIMEOUT
) -> dict:
    """Get transaction based on index in list of transactions in a block by
    block hash.

    Parameters
    ----------
    block_hash: str
        Block hash for transaction
    tx_index: int
        Transaction index to fetch (starts from 0)
    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    dict, see get_transaction_by_hash for description

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://api.woopchain.com/#7c7e8d90-4984-4ebe-bb7e-d7adec167503
    """
    method = "wikiv2_getTransactionByBlockHashAndIndex"
    params = [ block_hash, tx_index ]
    try:
        return rpc_request(
            method,
            params = params,
            endpoint = endpoint,
            timeout = timeout
        )[ "result" ]
    except KeyError as exception:
        raise InvalidRPCReplyError( method, endpoint ) from exception


def get_transaction_by_block_number_and_index(
    block_num,
    tx_index,
    endpoint = DEFAULT_ENDPOINT,
    timeout = DEFAULT_TIMEOUT
) -> dict:
    """Get transaction based on index in list of transactions in a block by
    block number.

    Parameters
    ----------
    block_num: int
        Block number for transaction
    tx_index: int
        Transaction index to fetch (starts from 0)
    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    dict, see get_transaction_by_hash for description

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://api.woopchain.com/#bcde8b1c-6ab9-4950-9835-3c7564e49c3e
    """
    method = "wikiv2_getTransactionByBlockNumberAndIndex"
    params = [ block_num, tx_index ]
    try:
        return rpc_request(
            method,
            params = params,
            endpoint = endpoint,
            timeout = timeout
        )[ "result" ]
    except KeyError as exception:
        raise InvalidRPCReplyError( method, endpoint ) from exception


def get_transaction_receipt(
    tx_hash,
    endpoint = DEFAULT_ENDPOINT,
    timeout = DEFAULT_TIMEOUT
) -> dict:
    """Get transaction receipt corresponding to tx_hash.

    Parameters
    ----------
    tx_hash: str
        Transaction receipt to fetch
    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    dict with the following keys:
        blockHash: :obj:`str` Block hash
        blockNumber: :obj:`int` Block number
        contractAddress: :obj:`str` Smart contract address
        culmulativeGasUsed: :obj:`int` Gas used for transaction
        from: :obj:`str` Sender wallet address
        gasUsed: :obj:`int` Gas used for the transaction
        logs: :obj:`list` List of logs, each being a dict with keys as follows:
            address, blockHash, blockNumber
            data, logIndex, removed
            topics, transactionHash, transactionIndex
        logsBloom :obj:`str` Bloom logs
        shardID :obj:`int` Shard ID
        status :obj:`int` Status of transaction (0: pending, 1: success)
        to :obj:`str` Receiver wallet address
        transactionHash :obj:`str` Transaction hash
        transactionIndex :obj:`int` Transaction index within block

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://api.woopchain.com/#0c2799f8-bcdc-41a4-b362-c3a6a763bb5e
    """
    method = "wikiv2_getTransactionReceipt"
    params = [ tx_hash ]
    try:
        return rpc_request(
            method,
            params = params,
            endpoint = endpoint,
            timeout = timeout
        )[ "result" ]
    except KeyError as exception:
        raise InvalidRPCReplyError( method, endpoint ) from exception


def send_raw_transaction(
    signed_tx,
    endpoint = DEFAULT_ENDPOINT,
    timeout = DEFAULT_TIMEOUT
) -> str:
    """Send signed transaction.

    Parameters
    ----------
    signed_tx: str
        Hex representation of signed transaction
    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    str
        Transaction hash

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint, or
    RPCError
        If transaction failed to be added to the pool

    API Reference
    -------------
    https://api.woopchain.com/#f40d124a-b897-4b7c-baf3-e0dedf8f40a0
    """
    params = [ signed_tx ]
    method = "wikiv2_sendRawTransaction"
    try:
        return rpc_request(
            method,
            params = params,
            endpoint = endpoint,
            timeout = timeout
        )[ "result" ]
    except KeyError as exception:
        raise InvalidRPCReplyError( method, endpoint ) from exception


def send_and_confirm_raw_transaction(
    signed_tx,
    endpoint = DEFAULT_ENDPOINT,
    timeout = DEFAULT_TIMEOUT
) -> list:
    """Send signed transaction and wait for it to be confirmed.

    Parameters
    ----------
    signed_tx: str
        Hex representation of signed transaction
    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    str
        Transaction, see get_transaction_by_hash for structure

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint, or
    RPCError
        If transaction failed to be added to the pool
    TxConfirmationTimedoutError
        If transaction could not be confirmed within the timeout period

    API Reference
    -------------
    https://api.woopchain.com/#f40d124a-b897-4b7c-baf3-e0dedf8f40a0
    """
    tx_hash = send_raw_transaction( signed_tx, endpoint = endpoint )
    start_time = time.time()
    while ( time.time() - start_time ) <= timeout:
        tx_response = get_transaction_by_hash( tx_hash, endpoint = endpoint )
        if tx_response is not None:
            block_hash = tx_response.get( "blockHash", "0x00" )
            unique_chars = "".join( set( list( block_hash[ 2 : ] ) ) )
            if unique_chars != "0":
                return tx_response
        time.sleep( random.uniform( 0.2, 0.5 ) )
    raise TxConfirmationTimedoutError(
        "Could not confirm transaction on-chain."
    )


###############################
# CrossShard Transaction RPCs #
###############################
def get_pending_cx_receipts(
    endpoint = DEFAULT_ENDPOINT,
    timeout = DEFAULT_TIMEOUT
) -> list:
    """Get list of pending cross shard transactions.

    Parameters
    ----------
    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    list of CX receipts, each a dict with the following keys
        commitBitmap: :obj:`str` Hex represenation of aggregated signature bitmap
        commitSig: :obj:`str` Hex representation of aggregated signature
        receipts: :obj:`list` list of dictionaries, each a cross shard transaction receipt
            amount: :obj:`int` Amount in ATTO
            from: :obj:`str` From address
            to: :obj:`str` From address
            shardId: :obj:`int` Originating shard ID
            toShardId: :obj:`int` Destination shard ID
            txHash: :obj:`str` Transation hash
        merkleProof: :obj:`dict` dictionary with the following keys:
            blockHash: :obj:`str` Block hash
            blockNum: :obj:`int` Block number
            receiptHash: :obj:`str` Transaction receipt hash
            shardHashes: :obj:`list` Shard hashes for shardIDs
            shardID: :obj:`int` Shard ID of originating block
            shardIDs: :obj:`list` To shard(s)
        header: :obj:`dict` with the following keys (those not noted below are legacy)
            shardID: :obj:`int` Originating shard ID
            hash: :obj:`str` Block header hash
            number: :obj:`int` Block number
            viewID: :obj:`int` View ID
            epoch: :obj:`int` Epoch number

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint, or
        if transaction failed to be added to the pool

    API Reference
    -------------
    https://api.woopchain.com/#fe60070d-97b4-458d-9365-490b44c18851
    """
    method = "wikiv2_getPendingCXReceipts"
    try:
        return rpc_request( method,
                            endpoint = endpoint,
                            timeout = timeout )[ "result" ]
    except KeyError as exception:
        raise InvalidRPCReplyError( method, endpoint ) from exception


def get_cx_receipt_by_hash(
    cx_hash,
    endpoint = DEFAULT_ENDPOINT,
    timeout = DEFAULT_TIMEOUT
) -> dict:
    """Get cross shard receipt by hash on the receiving shard end point.

    Parameters
    ----------
    cx_hash: str
        Hash of cross shard transaction receipt
    endpoint: :obj:`str`, optional
        Receiving endpoint for the RPC query
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    dict with the following keys
        blockHash: :obj:`str` Block hash
        blockNumber: :obj:`int` Block number
        hash: :obj:`str` Transaction hash
        from: :obj:`str` Sender wallet address
        to: :obj:`str` Receiver wallet address
        shardID: :obj:`int` From shard
        toShardID: :obj:`int` To shard
        value: :obj:`int` Amount transferred in Atto
    None if cx receipt hash not found

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://api.woopchain.com/#3d6ad045-800d-4021-aeb5-30a0fbf724fe
    """
    params = [ cx_hash ]
    method = "wikiv2_getCXReceiptByHash"
    try:
        return rpc_request(
            method,
            params = params,
            endpoint = endpoint,
            timeout = timeout
        )[ "result" ]
    except KeyError as exception:
        raise InvalidRPCReplyError( method, endpoint ) from exception


def resend_cx_receipt(
    cx_hash,
    endpoint = DEFAULT_ENDPOINT,
    timeout = DEFAULT_TIMEOUT
) -> bool:
    """Resend the cross shard receipt to the receiving shard to re-process if
    the transaction did not pay out.

    Parameters
    ----------
    cx_hash: :obj:`str`
        Hash of cross shard transaction receipt
    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    bool
        True if the cross shard receipt was succesfully resent

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://api.woopchain.com/#c658b56b-d20b-480d-b71a-b0bc505d2164
    """
    method = "wikiv2_resendCx"
    params = [ cx_hash ]
    try:
        return rpc_request(
            method,
            params = params,
            endpoint = endpoint,
            timeout = timeout
        )[ "result" ]
    except KeyError as exception:
        raise InvalidRPCReplyError( method, endpoint ) from exception


############################
# Staking Transaction RPCs #
############################
def get_staking_transaction_by_hash(
    tx_hash,
    endpoint = DEFAULT_ENDPOINT,
    timeout = DEFAULT_TIMEOUT
) -> dict:
    """Get staking transaction by hash.

    Parameters
    ----------
    tx_hash: str
        Hash of staking transaction to fetch
    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    dict with the following keys
        blockHash: :obj:`str` Block hash in which transaction was finalized
        blockNumber: :obj:`int` Block number in which transaction was finalized
        from: :obj:`str` Sender wallet address
        timestamp: :obj:`int` Unix time at which transaction was finalized
        gas: :obj:`int` Gas limit of transaction
        gasPrice: :obj:`int` Gas price of transaction in Atto
        hash: :obj:`str` Transaction hash
        nonce: :obj:`int` Wallet nonce of transaction
        transactionIndex: :obj:`int` Staking transaction index within block
        type: :obj:`str` Type of staking transaction
        msg: :obj:`dict` Staking transaction data, depending on the type of staking transaction
        r: :obj:`str` First 32 bytes of the transaction signature
        s: :obj:`str` Next  32 bytes of the transaction signature
        v: :obj:`str` Recovery value + 27, as hex string

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://api.woopchain.com/#296cb4d0-bce2-48e3-bab9-64c3734edd27
    """
    method = "wikiv2_getStakingTransactionByHash"
    params = [ tx_hash ]
    try:
        return rpc_request(
            method,
            params = params,
            endpoint = endpoint,
            timeout = timeout
        )[ "result" ]
    except KeyError as exception:
        raise InvalidRPCReplyError( method, endpoint ) from exception


def get_staking_transaction_by_block_hash_and_index(
    block_hash,
    tx_index,
    endpoint = DEFAULT_ENDPOINT,
    timeout = DEFAULT_TIMEOUT
) -> dict:
    """Get staking transaction by block hash and transaction index.

    Parameters
    ----------
    block_hash: str
        Block hash for transaction
    tx_index: int
        Staking transaction index to fetch (starts at 0)
    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    dict, see get_staking_transaction_by_hash for description

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://api.woopchain.com/#ba96cf61-61fe-464a-aa06-2803bb4b358f
    """
    method = "wikiv2_getStakingTransactionByBlockHashAndIndex"
    params = [ block_hash, tx_index ]
    try:
        return rpc_request(
            method,
            params = params,
            endpoint = endpoint,
            timeout = timeout
        )[ "result" ]
    except KeyError as exception:
        raise InvalidRPCReplyError( method, endpoint ) from exception


def get_staking_transaction_by_block_number_and_index(
    block_num,
    tx_index,
    endpoint = DEFAULT_ENDPOINT,
    timeout = DEFAULT_TIMEOUT
) -> dict:
    """Get staking transaction by block number and transaction index.

    Parameters
    ----------
    block_num: int
        Block number for transaction
    tx_index: int
        Staking transaction index to fetch
    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    dict, see get_staking_transaction_by_hash for description

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://api.woopchain.com/#fb41d717-1645-4d3e-8071-6ce8e1b65dd3
    """
    method = "wikiv2_getStakingTransactionByBlockNumberAndIndex"
    params = [ block_num, tx_index ]
    try:
        return rpc_request(
            method,
            params = params,
            endpoint = endpoint,
            timeout = timeout
        )[ "result" ]
    except KeyError as exception:
        raise InvalidRPCReplyError( method, endpoint ) from exception


def send_raw_staking_transaction(
    raw_tx,
    endpoint = DEFAULT_ENDPOINT,
    timeout = DEFAULT_TIMEOUT
) -> str:
    """Send signed staking transaction.

    Parameters
    ----------
    raw_tx: str
        Hex representation of signed transaction
    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    str
        Transaction hash

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint, or
    RPCError
        If transaction failed to be added to the pool

    API Reference
    -------------
    https://api.woopchain.com/#e8c17fe9-e730-4c38-95b3-6f1a5b1b9401
    """
    method = "wikiv2_sendRawStakingTransaction"
    params = [ raw_tx ]
    try:
        return rpc_request(
            method,
            params = params,
            endpoint = endpoint,
            timeout = timeout
        )[ "result" ]
    except KeyError as exception:
        raise InvalidRPCReplyError( method, endpoint ) from exception


def send_and_confirm_raw_staking_transaction(
    signed_tx,
    endpoint = DEFAULT_ENDPOINT,
    timeout = DEFAULT_TIMEOUT
) -> list:
    """Send signed staking transaction and wait for it to be confirmed.

    Parameters
    ----------
    signed_tx: str
        Hex representation of signed staking transaction
    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    str
        Transaction, see get_transaction_by_hash for structure

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint, or
    RPCError
        If transaction failed to be added to the pool
    TxConfirmationTimedoutError
        If transaction could not be confirmed within the timeout period

    API Reference
    -------------
    https://api.woopchain.com/#e8c17fe9-e730-4c38-95b3-6f1a5b1b9401
    """
    tx_hash = send_raw_staking_transaction( signed_tx, endpoint = endpoint )
    start_time = time.time()
    while ( time.time() - start_time ) <= timeout:
        tx_response = get_staking_transaction_by_hash(
            tx_hash,
            endpoint = endpoint
        )
        if tx_response is not None:
            block_hash = tx_response.get( "blockHash", "0x00" )
            unique_chars = "".join( set( list( block_hash[ 2 : ] ) ) )
            if unique_chars != "0":
                return tx_response
        time.sleep( random.uniform( 0.2, 0.5 ) )
    raise TxConfirmationTimedoutError(
        "Could not confirm transaction on-chain."
    )
