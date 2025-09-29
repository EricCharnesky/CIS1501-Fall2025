import math
import random

# tells python it's ok to be empty
def some_function():
    pass

# type suggestions
def print_triangle(size : int, character : str):
    for row in range(1, size+1):
        print(row*character)

# be careful of passing lists by value ( the address where it is in memory )
def list_fun(some_list):
    for index in range(len(some_list)):
        some_list[index] = some_list[index].upper()
    some_list.append("Eric was here")

# ax^2 + bx + c = 0 - pass by value
def get_intercepts(a : float, b : float, c : float):
    determinant = b*b - 4*a*c
    if determinant < 0:
        return "No intercepts"
    first_intercept = (-b + math.sqrt(determinant))/(2*a)
    second_intercept = (-b - math.sqrt(determinant))/(2*a)
    a = 0
    b = 0
    c = 0
    return first_intercept, second_intercept

def get_two_numbers_within_range(low : int, high : int):
    first_number = random.randint(low, high)
    second_number = random.randint(low, high)
    return first_number, second_number
    # return ( first_number, second_number )


def get_valid_input(valid_options : tuple[str]):
    choice = input(f"Enter a choice {valid_options}")
    while choice not in valid_options:
        print("Invalid entry, please try again dummy")
        choice = input(f"Enter a choice {valid_options}")
    return choice


def happy_monday():
    print("Happy Monday")
    print("Is it Friday yet?")

print_triangle(10, 10)
print_triangle(7, ".")

my_list = ['apples', 'bananas', 'cucumbers']

get_valid_input(my_list)
print(my_list)
# passes a copy
# list_fun(my_list[:])
list_fun(my_list)
print(my_list)

a = float(input("Enter your a value"))
b = float(input("Enter your b value"))
c = float(input("Enter your c value"))

print(get_intercepts(a,b,c))
print(a,b,c)

result = get_two_numbers_within_range(1, 100)
first = result[0]
second = result[1]

# automatic unpacking of a tuple
one, two = get_two_numbers_within_range(1, 100)

grades = { "Eric" : "A"}

for name, grade in grades.items():
    print(name, grade)

value = happy_monday()
print(value)

choices = ("up", 'down', 'left', 'right')
direction = get_valid_input(choices)
some_number = int(input("Enter a number"))
if direction == 'up':
    print("You go up")
elif direction == 'down':
    print("You go down")

def play_again():
    return get_valid_input(("y", "n"))

def get_users_throw():
    return get_valid_input(("rock", "paper", "scissors"))

def get_random_computer_throw():
    computer_throw = random.randint(1,3)
    if computer_throw == 1:
        return "rock"
    if computer_throw == 2:
        return "paper"
    return "scissors"

def determine_win_loss_draw(users_throw, computer_throw):
    if users_throw == computer_throw:
        return "draw!"
    if users_throw == 'rock' and computer_throw == 'scissors' \
        or users_throw == 'paper' and computer_throw == 'rock' \
        or users_throw == 'scissors' and computer_throw == 'paper':
        return "You win!"
    return "you lose!"


while play_again() == 'y':
    users_throw = get_users_throw()
    computer_throw = get_random_computer_throw()
    print(determine_win_loss_draw(users_throw, computer_throw))
