from .item import Item
class Electronics(Item):
    def __init__(self, id=None, type="Unknown", condition=0, age=None):
        super().__init__(id, condition, age)
        self.category = "Electronics"
        self.type = type

    def __str__(self):
        return (f"An object of type {self.get_category()} with id {self.id}. "
                f"This is a {self.type} device.")
