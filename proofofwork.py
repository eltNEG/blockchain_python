from hashlib import sha256


class ProofOfWork(object):
    targetbits = 16

    def __init__(self, block, target):
        self.block = block
        self.target = target

    def prepare_data(self, nonce):
        data = (
            self.block.prev_block_hash +
            self.block.data +
            hex(self.block.timestamp)[2:] +
            hex(self.targetbits)[2:] +
            hex(nonce)[2:]
        )
        return data

    def run(self):
        print(f'Mining the block containing {self.block.data}')
        for nonce in range(2**31 - 1):
            data = self.prepare_data(nonce)
            hash = sha256(data.encode("utf-8")).hexdigest()
            print(hash, end='\r')
            if int(hash, 16) < self.target:
                break
        print(f'{hash}\n')
        return (hash, nonce)

    @staticmethod
    def new_proofofwork(block):
        # or 2 ** (256-targetbits)
        target = 1 << (256 - ProofOfWork.targetbits)
        return ProofOfWork(block, target)

    @staticmethod
    def validate(block):
        pow = ProofOfWork.new_proofofwork(block)
        data = pow.prepare_data(block.nonce)
        hash = sha256(data.encode("utf-8")).hexdigest()
        return int(hash, 16) < pow.target
