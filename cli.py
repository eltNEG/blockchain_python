import argparse
from blockchain import Blockchain
from proofofwork import ProofOfWork


class Cli(object):
    def __init__(self):
        self.blockchain = Blockchain.new_blockchain()

    def addblock(self, data: str = ""):
        self.blockchain.add_block(data)
        print("success!")

    def print_chain(self):
        bci = self.blockchain.iterator()
        while True:
            block = bci.next()
            print(block)
            print(f"POW: {ProofOfWork.validate(block)}")
            if len(block.prev_block_hash) == 0:
                break

    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "addblock", nargs="?", help="Add a block to the block chain", type=str)
        parser.add_argument("printchain", nargs="?",
                            help="Print all the blocks in the database")
        parser.add_argument(
            "-d", "--data", help="Add block data to the blockchain", type=str)
        args = parser.parse_args()
        if args.addblock == "addblock":
            self.addblock(args.data)
        elif args.addblock == "printchain":
            self.print_chain()
