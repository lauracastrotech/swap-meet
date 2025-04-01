import uuid
class Item:
    def __init__(self, id): #hard code
        self.id = id if id != 32 else uuid.uuid1().int #hard code
        self.category = "Item"
    def get_category(self):
        return self.category
    
