class Vendor():
   def __init__(self, inventory = None):
      
      self.inventory = [] if inventory is None else inventory

   def add(self, item):
      self.inventory.append(item)
      return item

   def remove(self,item):
      if not item in self.inventory:
         return False
      self.inventory.remove(item)
      return item

   def get_by_id(self, id):
      for item in self.inventory:
         if item.id == id:
               return item
      return None
   
   def get_by_category(self, category):
      items_with_category = []
      if not self.inventory:
         return items_with_category
      for item in self.inventory:
         if item.get_category() == category:
            items_with_category.append(item)
      return items_with_category
   
   def get_best_by_category(self, category):
      list_items_with_category = self.get_by_category(category)
      if not list_items_with_category:
         return None
      return max(list_items_with_category, key=lambda item: item.condition)

   def swap_items(self, other_vendor, my_item, their_item):
      if my_item not in self.inventory or their_item not in other_vendor.inventory:
         return False
      self.add(their_item)
      other_vendor.add(my_item)
      self.remove(my_item)
      other_vendor.remove(their_item)
      return True
   
   def swap_first_item(self, other_vendor):
      if not self.inventory or not other_vendor.inventory:
         return False
      my_item = self.inventory[0]
      their_item = other_vendor.inventory[0]
      return self.swap_items(other_vendor, my_item, their_item)
   
   def swap_best_by_category(self, other_vendor, my_priority, their_priority):

      my_best_item = other_vendor.get_best_by_category(my_priority)
      their_best_item = self.get_best_by_category(their_priority)
      if my_best_item and their_best_item:
         # swap items 
         self.swap_items(other_vendor, their_best_item, my_best_item)
         # remove my item
         self.remove(their_best_item)
         # remove their item
         other_vendor.remove(my_best_item)
         return True
      return False
      
      

