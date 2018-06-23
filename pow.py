from hashlib import sha256
import sys

# target_bits on 24 is insanely takes long for python
# 18 bits for bitcoin
target_bits = 18
# python python supports arbitrarily large integers naturally
target = 1
target = target << (256 - target_bits) # 2**(256-target_bits)

class ProofOfWork():

  def __init__(self, _block):
      self.block = _block


  def new_proof_of_work(self, _block):


      pow = ProofOfWork(_block)

      return pow

  def prepare_data(self, _nonce: int):
      hash_int = 0
      hash = bytes(32)
      data = ''.join([str(self.block.PrevBlockHash) + self.block.Data + hex(int(self.block.Timestamp))[2:] + hex(target_bits)[2:] + hex(_nonce)[2:]])

      return data

  def run(self):
      nonce = 0
      while(nonce < sys.maxsize):

          data = self.prepare_data(nonce)
          hash = sha256(data.encode()).hexdigest()
          print("Hash: %s on trial %d" %  (hash, nonce))
          print(target)
          print(nonce)
          hash_int = int(hash, 16)
          if(hash_int < target):
              break
          nonce += 1

          print("\n\n")

      return nonce, hash




