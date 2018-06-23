from time import time
import json
from hashlib import sha256
from pow import *

class Block():
    def __init__(self, _timestamp, _data,  _prevblockhash, _hash):
        self.Timestamp = _timestamp
        self.Data = _data
        self.PrevBlockHash = _prevblockhash
        self.Hash = _hash

    # NewBlock creates and returns Block
    def new_block(self, _data: str, _prevblockhash: bytearray):
      block = Block(time(), _data, _prevblockhash, b'')
      print(block)
      pow = ProofOfWork(block)
      pow.new_proof_of_work(block)
      nonce, hash = pow.run()

      block.Hash = str(hash)
      block.Nonce = nonce

      return block

    def set_hash(self):
      timestamp = int(self.Timestamp)
      headers = str(timestamp) + str(self.PrevBlockHash) + self.Data
      self.Hash = sha256(headers.encode()).hexdigest()

