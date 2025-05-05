import uuid
class Item:
   def __init__(self, id=None, condition=0, age=None):
      self.id = uuid.uuid1().int if id is None else id
      self.category = "Item"
      self.condition = condition
      self.age = age
   
   def get_category(self):
      return self.__class__.__name__
   
   def __str__(self):
      return f"An object of type {self.get_category()} with id {self.id}."
   
   def condition_description(self):
      match(self.condition):
         case 0.0:
            return "It sucks!"
         case 1.0:
            return "Even my cat wouldn't pay for this."
         case 2.0:
            return "This is dull. I've seen trash with more personality."
         case 3.0:
            return "Meh. Like decaf coffee — fine, but why?"
         case 4.0:
            return "Now we're talking! A little weird, but charming"
         case 5.0:
            return "Legendary find! Someone's grandma is crying right now."