from shopping_cart import ShoppingCart
from item import Item

cart = ShoppingCart()

item_name = ""

while item_name.lower() != "quit":

    item_name = input("Enter an item to buy or quit")
    if item_name.lower() != 'quit':
        quantity = int(input("Enter the quantity"))
        unit_price = float(input("Enter the unit price"))
        cart.add_item(Item(item_name, quantity, unit_price))

print(cart.receipt())