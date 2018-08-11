"""Block"""
import pickle
from time import time
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

    def serialise(self) -> bytes:
        return pickle.dumps(self)

    @staticmethod
    def deserialise_block(serilised_block: bytes):
        return pickle.loads(serilised_block)

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


def main():
    """Test Block hash with hashes from blockchain_go"""
    block = Block.new_block("Genesis Block", "")
    print(block)
    print(Block.new_genesis_block())

    block1 = Block(1533814510, "Genesis Block", "", "", 0)
    print(block1)
    block2 = Block(1533814510, "Send 1btc to eltneg", block1.hash, "", 0)

    print(block2)


if __name__ == '__main__':
    main()
