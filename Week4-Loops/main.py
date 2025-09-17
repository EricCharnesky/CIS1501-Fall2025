import random

rows = int(input("Enter the number of rows for a rectangle"))
columns = int(input("Enter the number of columns for a rectangle"))

# lets row happen rows # of times
for row in range(rows):
    for column in range(columns):
        print('*', end="") # makes it not go down a line after printing
    print()


print()
height = int(input("Enter the height of a right angle triangle"))
print()

for row in range(height):
    for column in range(row+1):
        print('*', end="")  # makes it not go down a line after printing
    print()


print()

base = int(input("Enter the base for your equilateral triangle"))

while base % 2 == 0:
    print("odd numbers only")
    base = int(input("Enter the base for your equilateral triangle"))

rows = (base + 1) // 2
spaces = base // 2
stars = 1

for row in range(rows):
    for space in range(spaces):
        print(' ', end='')
    for star in range(stars):
        print('*', end='')
    print()
    spaces -= 1
    stars += 2


# base 9 - spaces 4
# base 7 - spaces 3
# base 5 - spaces 2
# base 3 - spaces 1


#     *     4 spaces
#    ***    3 spaces
#   *****   2 spaces
#  *******  1 spaces
# ********* 0 spaces
#
# base 3 - 2 rows
# base 5 - 3 rows
# base 7 - 4 rows
# base 9 - 5 rows
# base 11 - 6
# base 13 - 7



name = input("Enter your name")
# for item in collection
for letter in name:
    letter = letter.upper()
    print(letter)

print(name)

alphabet = [ 'a', 'b', 'c', 'd', 'e' ]

# essentially a copy of the item - read only loop
for letter in alphabet:
    letter = letter.upper()
    print(letter)

print(alphabet)


for index in range(len(alphabet)):
    alphabet[index] = alphabet[index].upper()


index = 0
while index < len(alphabet):
    alphabet[index] = alphabet[index].upper()
    index += 1

print(alphabet)

play_again = 'y'

while play_again == 'y':

    max_number = int(input("Enter the max number to guess"))
    while max_number <= 0 or max_number > 1_000_000:
        print("Enter a number greater than 1 and less than 1,000,000")
        max_number = int(input("Enter the max number to guess"))

    number_to_guess = random.randint(1, max_number)

    guess = int(input(f"Guess a number 1-{max_number}: "))

    # pre-test loop - if it's true, it runs - when it's all done, check again
    while guess != number_to_guess:

        if guess < number_to_guess:
            print("Too low!")
        else:
            print("Too high!")

        guess = int(input(f"Guess a number 1-{max_number}: "))


    print("You guessed it!")

    play_again = input("Do you want to play again? (y/n)")

    valid_options = ('y', 'n')
    while play_again not in valid_options:
        print("Please enter only y or n")
        play_again = input("Do you want to play again? (y/n)")
