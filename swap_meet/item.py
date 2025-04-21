import uuid
class Item:
   def __init__(self, id=None, condition=0, age=None):
      self.id = uuid.uuid1().int if id is None else id
      self.category = "Item"
      self.condition = condition
      self.age = age
   
   def get_category(self):
      return self.category
   
   def __str__(self):
      return f"An object of type {self.get_category()} with id {self.id}."
   
   def condition_description(self):
      match(self.condition):
         case 0.0:
            return "It sucks!"
         case 1.0:
            return "Not worth it."
         case 2.0:
            return "This looks rough."
         case 3.0:
            return "Good but not great."
         case 4.0:
            return "Such a deal."
         case 5.0:
            return "You're in luck, this is a steal."