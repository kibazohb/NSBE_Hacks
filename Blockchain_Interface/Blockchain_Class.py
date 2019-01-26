import datetime

"""
    BLOCK FORMAT
    
    "index" : <int>
    "date" : <datetime.date>
    "transaction" : [{"owner" : <string>, "officer" : <string>, "coordinates" : [<float>, <float>], "price" : <float>}]
    
    "prev_hash" : <string>
    
    """

class Block:
    def __init__(self, owner, officer, longitude, latitude, price):
        self.index = None
        self.date = None
        self.transaction = [
                            {"owner" : owner,
                            "officer" : officer,
                            "longitude" : longitude,
                            "latitude" : latitude,
                            "price" : price}
                            ]
        self.prev_hash = None
    
    def update_index(self, index):
        self.index = index
    
    def update_date(self):
        self.date = datetime.date
    
    def add_transaction(self, owner, officer, price):
        self.transaction.append({
                                "owner" : owner,
                                "officer" : officer,
                                "longitude" : self.transaction[0]["longitude"],
                                "latitude" : self.transaction[0]["latitude"],
                                "price" : price
                                })
    
    def print_receipt(self):
        print("DATE: ", self.date,
              "\nOWNER:", self.transaction[-1]["owner"],
              "\nOFFICER: ", self.transaction[-1]["officer"],
              "\nCOORDINATES: ", self.transaction[-1]["longitude"], ", ", self.transaction[-1]["latitude"],
              "\nPRICE: ", self.transaction[-1]["price"])



class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
    
    def new_block(self, owner, officer, longitude, latitude, price):
        self.chain.append(Block(owner, officer, longitude, latitude, price))
        self.index = len(self.chain) - 1 if len(self.chain) > 0 else 0
        self.date = datetime.date
    
    
    def new_transaction(self, owner, officer, price):
        self.chain[-1].add_transaction(owner, officer, price)
        self.chain[-1].print_receipt()
    
    @staticmethod
    def hash(block):
        # Hashes a Block
        pass
    
    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass


