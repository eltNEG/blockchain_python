from time import time
import json
from hashlib import sha256
from pow import *
import pickle

class Block():
    def __init__(self, _timestamp, _data,  _prevblockhash, _bits):
        self.Timestamp = _timestamp
        self.Data = _data
        self.PrevBlockHash = _prevblockhash
        self.Bits = _bits


    # new_block creates and returns Block
    def new_block(self, _data: str, _prevblockhash: bytearray, _bits: int):
      block = Block(time(), _data, _prevblockhash, _bits)
      pow = ProofOfWork(block)
      nonce, hash, next_required_bits = pow.run()

      # Add new properties for mined block
      block.Hash = hash
      block.Nonce = nonce
      block.NextRequiredBits = next_required_bits

      return block

    # serialize serializes Block
    def serialize(self):
        return pickle.dumps(self)

    # deserialize deserializes block
    def deserialize(self, _encoded : str):
        return pickle.loads(_encoded)
