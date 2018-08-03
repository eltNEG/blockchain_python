from time import time
import json
from hashlib import sha256
from pow import *
import pickle

class Block():
    def __init__(self, _timestamp, _data,  _prevblockhash, _hash):
        self.Timestamp = _timestamp
        self.Data = _data
        self.PrevBlockHash = _prevblockhash
        self.Hash = _hash

    # new_block creates and returns Block
    def new_block(self, _data: str, _prevblockhash: bytearray):
      block = Block(time(), _data, _prevblockhash, b'')
      pow = ProofOfWork(block)
      pow.new_proof_of_work(block)
      nonce, hash = pow.run()

      # Add new properties for mined block
      block.Hash = str(hash)
      block.Nonce = nonce

      return block

    # serialize serializes Block
    def serialize(self, _block: object):
        return pickle.dumps(_block)

    # deserialize deserializes block
    def deserialize(self, _str: bytes):
        return pickle.loads(_str)
