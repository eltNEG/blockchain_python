from hashlib import sha256
import sys
from tqdm import trange
from time import time




class ProofOfWork():

  def __init__(self, _block):
      self.block = _block
      # 18 bits for bitcoin
      self.target_bits = 18
      # target value
      self.target = 1 << (256 - self.target_bits)
      # Time interval for each block generation in second
      self.interval = 15

  def set_difficulty(self, _interval: int):
      if _interval < self.interval:
          self.target_bits += 1
          self.target = 1 << (256 - self.target_bits)
          print("Increase difficulty")

      elif _interval > self.interval:
          self.target_bits -= 1
          self.target = 1 << (256 - self.target_bits)
          print("Decrease difficulty")


  def new_proof_of_work(self, _block):


      pow = ProofOfWork(_block)

      return pow

  def prepare_data(self, _nonce: int):
      hash_int = 0
      hash = bytes(32)
      data = ''.join([str(self.block.PrevBlockHash) + self.block.Data + hex(int(self.block.Timestamp))[2:] + hex(self.target_bits)[2:] + hex(_nonce)[2:]])

      return data

  def run(self):
      nonce = 0
      for i in trange(sys.maxsize, desc="Mining at nonce {i}"):
          # Get flattened data for generating block hash
          data = self.prepare_data(nonce)
          hash = sha256(data.encode()).hexdigest()
          hash_int = int(hash, 16)
          if(hash_int < self.target):
              break
          nonce += 1

      # Set target_bits based on elapsed time for mining
      elapsed = time()

      mine_interval = int(elapsed - self.block.Timestamp)

      self.set_difficulty(mine_interval)


      return nonce, hash
