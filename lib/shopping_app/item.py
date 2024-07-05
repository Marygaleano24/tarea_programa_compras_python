from ownable import Ownable

class Item:
    instances = []

    def __init__(self, name, price, owner=None):
        self.name = name
        self.price = price
        self.set_owner(owner)  # Llama al método set_owner si existe
        Item.instances.append(self)

    def label(self):
        return {"name": self.name, "price": self.price}

    def set_owner(self, owner):
        # Implementa la lógica para establecer el propietario (owner) del ítem
        # Por ejemplo, puedes asignar el valor directamente o realizar otras acciones necesarias.
        self.owner = owner

    @staticmethod
    def item_all():
        return Item.instances
