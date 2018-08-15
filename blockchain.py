from block import Block
import plyvel
import logging



# LevelDB supports its own built-in iterator
# Therefore Custom Iterator is not needed

class Blockchain(Block):


    def __init__(self, _db_file: str):
        self.db = plyvel.DB(_db_file, create_if_missing=True)
        self.iterator = self.db.raw_iterator()


    def add_block(self, _data: str):
        self.iterator.seek_to_last()
        last_hash = self.iterator.key()
        last_bit = self.deserialize(self.iterator.value()).NextRequiredBits
        new_block = self.new_block(_data, last_hash, last_bit)
        self.db.put(new_block.Hash.encode(), new_block.serialize())
        tip = new_block.Hash.encode()
        self.db.close()

        return self


    def new_genesis_block(self):
        return self.new_block( "Genesis block", b'Genesis', 18)


    def new_blockchain(self):
        # Null check for DB's content
        self.iterator.seek_to_first()
        if self.iterator.valid():
            self.iterator.seek_to_first()
            print("The chain is already stored")
            return self
        else:
            print("No existing blockchain found. Create Genesis first.")
            genesis = self.new_genesis_block()
            self.db.put(genesis.Hash.encode(), genesis.serialize())
            tip = genesis.Hash.encode()
            return self
