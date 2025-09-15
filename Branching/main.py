import random


item_cost = float(input("Enter the cost of your item"))


if item_cost < 800:
    tariff_cost = 0
else:
    tariff_cost = item_cost * .1

tariff_cost = 0 if item_cost < 800 else item_cost * .1




orders = { 'DQPC' : 10, 'Fries' : 7, 'McNuggets' : 10 }

print(f'id of orders: {id(orders)}')

more_orders = { 'DQPC' : 10, 'Fries' : 7, 'McNuggets' : 10 }


print(f'id of more_orders: {id(more_orders)}')


print(f'orders is more_orders {orders is more_orders}')

more_orders = orders

print(f'id of orders: {id(orders)}')

print(f'id of more_orders: {id(more_orders)}')

print(f'orders is more_orders {orders is more_orders}')

customer_order = input(f"What do you want to order? {list(orders.keys())}")
if customer_order not in orders:
    print("Sir this is a wendy's")
else:
    orders[customer_order] += 1

print(orders)

# by default, the membership operator looks for keys!
if 10 in orders:
    print("Something was ordered 10 times")

if 10 in orders.values():
    print("Something was ordered 10 times")

sentence = input("Enter a word to count the Rs")

print(f'{sentence} has the letter r {sentence.lower().count('r')} times')
print(sentence)


email_address = input("Enter your email address")

valid_top_level_domains = ( '.com', '.net', '.org', '.edu' )

# string slicing - we'll come back to this - this gets the last 4 characters
if email_address[-4:] not in valid_top_level_domains or "@" not in email_address:
    email_address = input("Enter a valid email address")




valid_options = ('rock', 'paper', 'scissors')

users_throw = input("Enter Rock Paper or Scissors!").lower()

if users_throw != 'rock' and users_throw != 'paper' and users_throw != 'scissors':
    users_throw = input("Try again, Enter Rock Paper or Scissors!")

if not (users_throw == 'rock' or users_throw == 'paper' or users_throw == 'scissors') :
    users_throw = input("Try again, Enter Rock Paper or Scissors!")

if users_throw not in valid_options:
    users_throw = input("Try again, Enter Rock Paper or Scissors!")


computer_throw_number = random.randint(1, 3)

if computer_throw_number == 1:
    computer_throw = 'rock'
elif computer_throw_number == 2:
    computer_throw = 'paper'
else:
    computer_throw = 'scissors'

if users_throw == computer_throw:
    print("You draw!")
elif (users_throw == 'rock' and computer_throw == 'scissors') or \
    (users_throw == 'paper' and computer_throw == 'rock') or \
    (users_throw == 'scissors' and computer_throw == 'paper'):
    print("You win!")
else:
    print("You lose!")


if users_throw == computer_throw:
    print("You draw!")
elif users_throw == 'rock' and computer_throw == 'scissors':
    print("rock crushes scissors")
elif users_throw == 'paper' and computer_throw == 'rock':
    print("paper covers rock")
elif users_throw == 'scissors' and computer_throw == 'paper':
    print("scissors cuts paper")
else:
    print("You lose!")

temperature = int(input("What's the temperature?"))

# found how to lowercase input from http://.....
weather = input("What's the weather like? (sunny, rainy, cloudy)").lower()

if temperature > 60:
    print("You don't need a jacket")
    if weather == 'sunny':
        print("Dont forget the sun screen")
    elif weather == 'rainy':
        print("Bring your umbrella")
else:
    print("You should have a hoodie")
    print("more advice from dad")

print("have a great wednesday!")

score = int(input("Enter your score 1-100"))

if score > 93:
    print("A")
elif score >= 90:
    print("A-")
elif score > 86:
    print("B+")
elif score > 83:
    print("B")
else:
    print("F")

if score > 93:
    print('A')
if 90 < score <= 93:
    print("A-")
if 93 >= score >= 90:
    print("A-")
if score <= 93 and score >= 90:
    print("A-")

# true and true == true
# true and false == false
# false and true == false
# false and false == false

# true or true == true
# true or false == true
# false or true == true
# false or false == false


print("Hope you like your score")
