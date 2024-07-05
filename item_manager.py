# Al incluir este módulo, podrás manipular las instancias de Item que posees.

from item import Item
from tabulate import tabulate

from itertools import groupby

def items_list(self):  # Devuelve todas las instancias de Item que posee (que tienen a sí mismo como propietario).
    items = [item for item in Item.item_all() if item.owner == self]
    return items

def pick_items(self, number, quantity):  # Devuelve las instancias de Item que posee, correspondientes al número y la cantidad especificada.
    items = filter(lambda num: num["number"] == number, _stock(self))
    items = list(items)
    if len(items) == 0:
        return []
    elif len(items[0]["items"]) < quantity:
        return []
    else:
        return items[0]["items"][0:quantity]

def show_items(self):  # Muestra el inventario de las instancias de Item que posee en formato de tabla con las columnas ["Número", "Nombre del artículo", "Precio", "Cantidad"].
    table_data = []
    for stock in _stock(self):
        table_data.append([stock['number'], stock['label']['name'], stock['label']['price'], len(stock['items'])])
    print(tabulate(table_data, headers=["Número", "Nombre del artículo", "Precio", "Cantidad"], tablefmt="grid"))  # Usa el módulo tabulate para mostrar el resultado en formato de tabla.

def _stock(self):  # Devuelve el inventario de las instancias de Item que posee.
    item_ls = self.items_list()
    item_ls.sort(key=lambda m: m.name)
    group_list = []
    for key, group in groupby(item_ls, key=lambda m: m.name):  # Agrupa las instancias de Item por su nombre.
        group_list.append(list(group))
    stock = []
    for index, item in enumerate(group_list):
        stock.append({"number": index, "label": {"name": item[0].name, "price": item[0].price}, "items": item})  # En "items" se almacenan las instancias de Item agrupadas.
    return stock
