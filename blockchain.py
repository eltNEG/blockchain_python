"""Blockchain"""
from block import Block
from leveldb import LevelDB, LevelDBError
from sys import exit

dbLocation: str = "blockchain_db"


class BlockchainIterator (object):
    """iterate over blockchain blocks"""

    def __init__(self, current_hash: bytes, db: LevelDB) -> None:
        """Iterate over blockchain blocks"""
        self.current_hash: bytes = current_hash
        self.db: LevelDB = db

    def next(self) -> Block:
        try:
            block: Block = Block.deserialise_block(self.db.Get(self.current_hash))
        except KeyError:
            print("An error occurred")
            exit(1)
        self.current_hash = bytes(block.prev_block_hash.encode())
        return block


class Blockchain(object):
    """Blockchain"""

    def __init__(self, tip: bytes, db: LevelDB) -> None:
        """Initialize blockchain which stores a list of blocks"""
        self.tip: bytes = tip
        self.db: LevelDB = db

    def add_block(self, _data: str):
        """saves provided data as a block in the blockchain"""
        try:
            lasthash: str = self.db.Get(b"tip").decode()
            new_block: Block = Block.new_block(_data, lasthash)
        except KeyError:
            print("An error occur")
            exit(1)
        try:
            tip: bytes = bytes(new_block.hash.encode())
            self.db.Put(tip, new_block.serialise())
            self.db.Put(b'tip', tip)
            self.tip = tip
        except LevelDBError as e:
            print(f"An error Occur:\n{e}")
            exit(1)

    def iterator(self) -> BlockchainIterator:
        return BlockchainIterator(self.tip, self.db)

    @staticmethod
    def new_blockchain():
        """creates a new Blockchain with genesis Block"""
        tip: bytes = ""
        db = LevelDB(dbLocation)
        try:
            tip = db.Get(b'tip')
        except KeyError:
            print("No existing blockchain found. Creating a new one...")
            genesis = Block.new_genesis_block()
            tip = bytes(genesis.hash.encode())
            try:
                db.Put(bytes(genesis.hash.encode()), genesis.serialise())
                db.Put(b'tip', bytes(genesis.hash.encode()), sync=True)
            except TypeError:
                print("Type error")
                exit(1)

        return Blockchain(tip, db)

    def __str__(self):
        return f"Last Hash: {self.tip.decode()}"


def main():
    """Tests"""
    bc = (Blockchain.new_blockchain())


if __name__ == '__main__':
    main()
