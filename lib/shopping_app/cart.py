from ownable import Ownable

class Cart(Ownable):
    from item_manager import show_items

    def __init__(self, owner):
        super().__init__()  # Llama al constructor de Ownable
        self.set_owner(owner)  # Asigna el propietario al carrito
        self.items = []  # Inicializa la lista de artículos en el carrito

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            print("Saldo insuficiente en la billetera del propietario del carrito.")
            return
        
        total = self.total_amount()
        for item in self.items:
            item.owner.wallet.deposit(item.price)  # Transfiere el precio del artículo a la billetera del propietario del artículo
            item.owner = self.owner  # Transfiere la propiedad del artículo al propietario del carrito

        # Deduce el monto total de la billetera del comprador
        self.owner.wallet.withdraw(total)
        
        # Deposita el monto total en la billetera del vendedor
        for item in self.items:
            item.owner.wallet.deposit(item.price)
        
        self.items = []  # Vacía el carrito después de la compra

        print("Compra realizada exitosamente.")
