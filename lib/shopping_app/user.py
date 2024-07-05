from wallet import Wallet

class User:
    from item_manager import show_items, items_list, pick_items, show_items

    def __init__(self, name):
        self.name = name
        self.wallet = Wallet(self)  # Cuando se genera una instancia de User o de una clase que hereda de User, tendrá una billetera que lo considere su propietario.
