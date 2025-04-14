from .item import Item
class Clothing(Item):
    def __init__(self, id = None, fabric = "Unknown", condition = 0, age = None):
        super().__init__(id, condition, age)
        self.category = "Clothing"
        self.fabric = fabric
    # def get_category(self):
    #     return "Clothing"
    def __str__(self):
        return (f"An object of type {self.get_category()} with id {self.id}. "
        f"It is made from {self.fabric} fabric.")
    
        # return self.__str__() + f"It is made from {self.fabric} fabric."