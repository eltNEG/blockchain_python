"""Blockchain"""
from blockchain import Blockchain


def main():
    """Test the blockchain"""
    bc = Blockchain.new_blockchain()
    bc.add_block("Send 1 BTC to Ivan")
    bc.add_block("Send 2 more BTC to Ivan")

    for block in bc.blocks:
        print("Prev. hash: %s" % (block.prev_block_hash))
        print("Data: %s" % (block.data))
        print("Hash: %s" % (block.hash))
        print("Timestamp: %s" % (block.timestamp))
        print("\n")


main()
