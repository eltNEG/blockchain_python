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


def main():
    """Test Block hash with hashes from blockchain_go"""
    block = Block.new_block("Genesis Block", "")
    print(block)
    print(Block.new_genesis_block())

    block1 = Block(1533814510, "Genesis Block", "", "")
    block1.sethash()
    print(block1)
    block2 = Block(1533814510, "Send 1btc to eltneg", block1.hash, "")

    block2.sethash()
    print(block2)


if __name__ == '__main__':
    main()
