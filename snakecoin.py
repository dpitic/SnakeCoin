import hashlib as hasher
import datetime as date


class Block(object):
    """
    SnakeCoin blockchain block.  Consists of an index, timestamp, data, hash of
    predecessor block and cryptographic hash of this block.  The cryptographic
    hash of this block contains the hash of the predecessor block.  This
    increases the integrity of the blockchain with each new block.
    """

    def __init__(self, index, timestamp, data, predecessor_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.predecessor_hash = predecessor_hash
        # This block's hash contains the predecessor block's hash.
        self.hash = self.hash_block()

    def hash_block(self):
        """
        Return a hash of this block.  The hash consists of the hash of the
        predecessor block.  This is done to increase the integrity of the
        blockchain, which increases with each new block added to the
        blockchain.  The chain of hashes acts as a cryptographic proof that
        helps ensure that once a block is added to the blockchain, it cannot
        be replaced or removed easily.
        """
        sha = hasher.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.predecessor_hash).encode('utf-8'))
        return sha.hexdigest()


def create_genesis_block():
    """
    Manually construct the genesis block with index zero and arbitrary
    predecessor hash.
    """
    return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block):
    """
    Generate succeeding block in the blockchain.  This block contains a
    reference to the immediately preceding block by storing that block's
    hash.
    """
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Block index:  " + str(this_index)
    predecessor_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, predecessor_hash)


def main():
    # Create the blockchain using a list data type and add the genesis block
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    # Number of blocks to create and add to the genesis block
    num_of_blocks_to_add = 20

    # Add blocks to the blockchain
    for i in range(0, num_of_blocks_to_add):
        new_block = next_block(previous_block)
        blockchain.append(new_block)
        previous_block = new_block

        # Log output
        print("Block #{} has been added to the blockchain."
              .format(new_block.index))
        print("Block hash: {}\n".format(new_block.hash))


if __name__ == '__main__':
    main()
