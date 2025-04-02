import uuid
class Item:
   def __init__(self, id = None):
      self.id = uuid.uuid1().int if id is None else id
      self.category = "Item"
   
   def get_category(self):
      return self.category
   
   def __str__(self):
      return f"An object of type Item with id {self.id}."
   
   
