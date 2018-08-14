"""Block"""
from time import time
from hashlib import sha256


class Block():
    """keeps block headers"""

    def __init__(self, _timestamp, _data, _prevblockhash, _hash):
        """Initialise block"""
        self.timestamp = _timestamp
        self.data = _data
        self.prev_block_hash = _prevblockhash
        self.hash = _hash

    @staticmethod
    def new_block(_data: str, _prevblockhash: str):
        """creates and returns Block"""
        block = Block(int(time()), _data, _prevblockhash, "")
        block.__set_hash()
        return block

    @staticmethod
    def new_genesis_block():
        """Creates genesis block"""
        return Block.new_block("Genesis Block", "")

    def __set_hash(self):
        headers = str(self.prev_block_hash) + self.data + str(self.timestamp)
        self.hash = sha256(headers.encode("utf-8")).hexdigest()

    def sethash(self):
        headers = str(self.prev_block_hash) + self.data + str(self.timestamp)
        self.hash = sha256(headers.encode("utf-8")).hexdigest()

    def __str__(self):
        return """
Timestamp: {}
Data:      {}
Prev.Hash: {}
Hash:      {}
""".format(self.timestamp, self.data, self.prev_block_hash, self.hash)
