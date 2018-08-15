from hashlib import sha256
import sys
from tqdm import trange
from time import time
from bitstring import BitArray



class ProofOfWork():

  def __init__(self, _block):
      self.block = _block
      # target value
      self.target = 1 << (256 - _block.Bits)
      # Time interval for each block generation in second
      self.interval = 15

  def adjust_difficulty(self, _interval: int):
      if _interval < self.interval:
          print("Increase difficulty")
          return self.block.Bits + 1

      elif _interval > self.interval:
          print("Decrease difficulty")
          return self.block.Bits - 1


  def prepare_data(self, _nonce: int):
      hash_int = 0
      hash = bytes(32)
      data = ''.join([str(self.block.PrevBlockHash) + self.block.Data + hex(int(self.block.Timestamp))[2:] + hex(self.block.Bits)[2:] + hex(_nonce)[2:]])

      return data


  def run(self):
      nonce = 0
      for i in trange(sys.maxsize, desc="Mining...."):
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


      next_required_bits = self.adjust_difficulty(mine_interval)


      # Change Hash to bitstring
      # hash = BitArray(hex=hash).bin

      return nonce, hash, next_required_bits

  def validate(self, _block):
      pow = ProofOfWork(_block)
      data = pow.prepare_data(_block.Nonce)
      hash = sha256(data.encode("utf-8")).hexdigest()
      return int(hash, 16) < 1 << (256 - _block.Bits)
