import uuid
class Item:
   def __init__(self, id = None):
      self.id = uuid.uuid1().int if id is None else id
      self.category = "Item"
   def get_category(self):
      return self.category
   
   

