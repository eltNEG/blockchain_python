from block import Block


class Blockchain(Block):

    def __init__(self, _blocks: list):
        self.blocks = _blocks

    def add_block(self, _data: str):
      prev_block = self.blocks[-1]
      new_block = self.new_block(_data, prev_block.Hash)
      self.blocks.append(new_block)

    def new_genesis_block(self):
      return self.new_block( "Genesis block", b'Genesis')


    def new_blockchain(self):
      return Blockchain([self.new_genesis_block()])
