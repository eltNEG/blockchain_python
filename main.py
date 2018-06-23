from blockchain import *

def main():
  bc = Blockchain([]).new_blockchain()

  bc.add_block("Send 1 BTC to Ivan")
  bc.add_block("Send 2 more BTC to Ivan")

  for block in bc.blocks:
    print("Prev. hash: %s\n" % (block.PrevBlockHash), type(block.PrevBlockHash))
    print("Data: %s\n" % (block.Data))
    print("Hash: %s\n" % (block.Hash))


main()
