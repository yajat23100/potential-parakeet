import hashlib
import jason
from time import time

class block():
    def_init_(self):
       self.chain = []
       self.new_tansaction = []
       self.count = 0
       self.new_block(previous_hash = "No Previous Hash. Since First Block")

    def new_block(self,previous_hash=None):
        block = {
            'Block No' : self.count,
            'timestamp' : time(),
            'transactions' : self.new_transaction or 'no transaction first block',
            'gassfee' : 0.1
            'previous_hash' : previous_hash
        }
        self.count = self.count + 1
        self.chain.append(block)

        string_object = jason.dump(blocks)
        block_string = string_object.encode()
        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        self.chain.append(("Current Hsh :", hex_hash))
        return block

blockchain = Block()
print(blockchain.chain)
