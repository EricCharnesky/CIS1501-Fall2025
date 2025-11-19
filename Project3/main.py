from shopping_cart import ShoppingCart
from item import Item
from taxable_item import TaxableItem

cart = ShoppingCart()

taxable_item = TaxableItem("Paper Plates", 100, .05, .06)

print(taxable_item.get_total_price())

cart.add_item(taxable_item)

item_name = ""

while item_name.lower() != "quit":

    item_name = input("Enter an item to buy or quit")
    if item_name.lower() != 'quit':
        quantity = int(input("Enter the quantity"))
        unit_price = float(input("Enter the unit price"))
        cart.add_item(Item(item_name, quantity, unit_price))

print(cart.receipt())