import random


#https://learn.zybooks.com/zybook/UMDEARBORNCIS1501CharneskyFall2025/chapter/5/section/13

roll_counts = {}


how_many_sides = int(input("How many sides are your dice?"))
how_many_dice = int(input("How many dice do you want to roll?"))
num_rolls = int(input("Enter number of rolls:\n"))

for number in range(how_many_dice, how_many_dice*how_many_sides+1):
    roll_counts[number] = 0

for i in range(num_rolls):
    roll_total = 0
    for dice in range(how_many_dice):
        roll_total += random.randint(1, how_many_sides)

    roll_counts[roll_total] += 1
    #print(f"Roll {i} is {roll_total} ({die1} + {die2})")

for roll in roll_counts:
    print(f'{roll}: {roll_counts[roll] / num_rolls * 100:.3f}%')





total = 0

# sentinel values - unusual invalid values to stop a loop
while True:
    receipt = float(input("Enter a receipt value or -1 to stop"))
    if receipt == -1:
        # hard stop of the loop, do not pass go, do not continue
        break # jump to the end of the loop, next line after
    total += receipt

print("this is the line after the loop")

students = ['Eric', 'Jeb', 'Vivi', 'Journey']
for number, name in enumerate(students):
    print(f'Student #{number}: {name}')

for number in range(1, 100):
    if number % 2: # shortcut for if number % 2 == 1 - because 1 is true
        continue # jump back to the loop header
    print(number)

for even_number in range(2, 100, 2): # 3rd thing is a count by value
    print(even_number)

for count_down in range(10, -1, -1):
    print(count_down)
print("blastoff!")



total = 0

# sentinel values - unusual invalid values to stop a loop
receipt = float(input("Enter a receipt value or -1 to stop"))
while receipt != -1:
    total += receipt
    receipt = float(input("Enter a receipt value or -1 to stop"))
else:
    print("Thanks for totaling your drawer! If you lost any money, we're taking it from your paycheck!")
gradebook = {}

# sentinel value to stop the loop
name = input("Enter a student name or QUIT to stop")
while name.upper() != 'QUIT':
    score = float(input(f"enter the score for {name}"))
    gradebook[name] = score
    name = input("Enter a student name or QUIT to stop")

number_of_students = int(input("How many students are in your class?"))

for student in range(number_of_students):
    name = input(f"Enter student #{student}'s name")
    score = float(input(f"enter the score for {name}"))
    gradebook[name] = score

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

for index, value in enumerate(alphabet):
    alphabet[index] = value.upper()


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
