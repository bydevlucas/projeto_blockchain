<<<<<<< HEAD
from datetime import datetime
from hashlib import sha256

class Block:
    def __init__(self, certificates, previous_hash):
        self.certificates = certificates
        self.previous_hash = previous_hash
        self.nonce = 0
        self.timestamp = datetime.now()
        self.hash = self.generate_hash()

    def print_content(self):
        print("Timestamp: ", self.timestamp)
        print("Certificates: ", self.certificates)
        print("Current Hash: ", self.generate_hash())
        print("Previous Hash: ", self.previous_hash)
        print("\n")

    def generate_hash(self):
        block_contents = (
            str(self.timestamp)
            + str(self.certificates)
            + str(self.previous_hash)
            + str(self.nonce)
        )
        block_hash = sha256(block_contents.encode())
        return block_hash.hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.all_certificates = []
        self.genesis_block()

    def genesis_block(self):
        certificates = []
        previous_hash = "0"
        self.chain.append(Block(certificates, previous_hash))

    def print_blocks(self):
        for i, block in enumerate(self.chain):
            print(f"Block {i}")
            block.print_content()

    def add_block(self, certificates):
        previous_block_hash = self.chain[-1].hash
        new_block = Block(certificates, previous_block_hash)
        self.chain.append(new_block)

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.generate_hash():
                print("The current hash of the block does not match the generated hash.")
                return False
            if previous.hash != previous.generate_hash():
                print("The previous block's hash does not match the stored hash.")
                return False
        return True

    def proof_of_work(self, block, difficulty=2):
        proof = block.generate_hash()
        while proof[:difficulty] != '0' * difficulty:
            block.nonce += 1
            proof = block.generate_hash()
        block.nonce = 0
        return proof
=======
from datetime import datetime
from hashlib import sha256

class Block:
    def __init__(self, certificates, previous_hash):
        self.certificates = certificates
        self.previous_hash = previous_hash
        self.nonce = 0
        self.timestamp = datetime.now()
        self.hash = self.generate_hash()

    def print_content(self):
        print("Timestamp: ", self.timestamp)
        print("Certificates: ", self.certificates)
        print("Current Hash: ", self.generate_hash())
        print("Previous Hash: ", self.previous_hash)
        print("\n")

    def generate_hash(self):
        block_contents = (
            str(self.timestamp)
            + str(self.certificates)
            + str(self.previous_hash)
            + str(self.nonce)
        )
        block_hash = sha256(block_contents.encode())
        return block_hash.hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.all_certificates = []
        self.genesis_block()

    def genesis_block(self):
        certificates = []
        previous_hash = "0"
        self.chain.append(Block(certificates, previous_hash))

    def print_blocks(self):
        for i, block in enumerate(self.chain):
            print(f"Block {i}")
            block.print_content()

    def add_block(self, certificates):
        previous_block_hash = self.chain[-1].hash
        new_block = Block(certificates, previous_block_hash)
        self.chain.append(new_block)

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.generate_hash():
                print("The current hash of the block does not match the generated hash.")
                return False
            if previous.hash != previous.generate_hash():
                print("The previous block's hash does not match the stored hash.")
                return False
        return True

    def proof_of_work(self, block, difficulty=2):
        proof = block.generate_hash()
        while proof[:difficulty] != '0' * difficulty:
            block.nonce += 1
            proof = block.generate_hash()
        block.nonce = 0
        return proof
>>>>>>> dcaf25c5e5290811ee816302ff867b98749dd2ca
