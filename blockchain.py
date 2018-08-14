"""Blockchain"""
from block import Block


class Blockchain(object):
    """Blockchain"""

    def __init__(self, _blocks: list):
        """Initialize blockchain which stores a list of blocks"""
        self.blocks = _blocks

    def add_block(self, _data: str):
        """saves provided data as a block in the blockchain"""
        prev_block = self.blocks[-1]
        new_block = Block.new_block(_data, prev_block.hash)
        self.blocks.append(new_block)

    @staticmethod
    def new_blockchain():
        """creates a new Blockchain with genesis Block"""
        return Blockchain([Block.new_genesis_block()])

    def __str__(self):
        return str(self.blocks)
