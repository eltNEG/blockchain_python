"""Blockchain"""
from blockchain import Blockchain
from proofofwork import ProofOfWork


def main():
    """Test the blockchain"""
    bc = Blockchain.new_blockchain()
    bc.add_block("Send 1 BTC to Ivan")
    bc.add_block("Send 2 more BTC to Ivan")

    for block in bc.blocks:
        print("\n")
        print(block)
        print("Valid POW: %s" % (ProofOfWork.validate(block)))


main()
