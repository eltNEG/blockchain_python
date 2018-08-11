"""Block"""
from time import time
from hashlib import sha256
from proofofwork import ProofOfWork


class Block():
    """keeps block headers"""

    def __init__(self, _timestamp, _data, _prevblockhash, _hash, nonce):
        """Initialise block"""
        self.timestamp = _timestamp
        self.data = _data
        self.prev_block_hash = _prevblockhash
        self.hash = _hash
        self.nonce = nonce

    @staticmethod
    def new_block(_data: str, _prevblockhash: str):
        """creates and returns Block"""
        block = Block(int(time()), _data, _prevblockhash, "", 0)
        pow = ProofOfWork.new_proofofwork(block)
        _hash, nonce = pow.run()
        block.hash = _hash
        block.nonce = nonce
        return block

    @staticmethod
    def new_genesis_block():
        """Creates genesis block"""
        return Block.new_block("Genesis Block", "")

    def __str__(self):
        return """
Timestamp: {}
Data:      {}
Prev.Hash: {}
Hash:      {}
nonce:     {}
""".format(self.timestamp, self.data, self.prev_block_hash, self.hash, self.nonce)
