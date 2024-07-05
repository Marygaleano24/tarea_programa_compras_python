from user import User
from cart import Cart
from ownable import Ownable

class Customer(User):

    def __init__(self, name):
        super().__init__(name)
        self.cart = Cart(self)  # Cuando se genera una instancia de Customer, tendrá un carrito que lo considere su propietario.

