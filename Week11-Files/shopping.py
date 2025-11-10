import os

store_name = input("What store do you want to make a shopping list for?")

erase = 'y'

if os.path.exists(f'{store_name}.txt'):
    erase = input(f"You already have a list for {store_name}, do you want to start over? y/n")

if erase == 'y':
    shopping_list = open(f'{store_name}.txt', 'w')
else:
    print(f"Current list for {store_name}")
    with open(f'{store_name}.txt') as current_list:
        print(current_list.read())
    shopping_list = open(f'{store_name}.txt', 'a')

item = ""

while item != "quit":
    item = input("Enter an item name or quit")
    if item != "quit":
        quantity = input("How many?")
        price = input("How much does 1 cost?")
        shopping_list.write(item + "\n")
        shopping_list.write(quantity + "\n")
        shopping_list.write(price + "\n")

shopping_list.close()

total_price = 0
with open(f'{store_name}.txt') as current_list:
    while True:
        item_name = current_list.readline()
        if not item_name:
            break

        quantity = int(current_list.readline())
        price = float(current_list.readline())
        total_price += quantity * price
print(f"Total price for your list: ${total_price:.2f}")

total_price = 0
with open(f'{store_name}.txt') as current_list:
    lines = current_list.readlines()

for index in range(0, len(lines), 3):
    item = lines[index]
    quantity = int(lines[index+1])
    price = float(lines[index+2])
    total_price += quantity * price
print(f"Total price for your list: ${total_price:.2f}")
