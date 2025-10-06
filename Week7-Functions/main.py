favorite_number = 42

def print_date(day=6, month=10, year=2025):
    print(f'{year}-{month}-{day}')

    # gets the global variable
    global favorite_number
    favorite_number = 20
    print(f"Your favorite number is {favorite_number}")

def print_rectangle(length, width):
    for row in range(length):
        print(width*"*")

def get_number_within_range(upper_bound, lower_bound = 1):
    number = int(input(f"enter a number between {lower_bound}-{upper_bound}"))
   #while number < lower_bound or number > upper_bound:
    while not lower_bound <= number <= upper_bound:
        number = int(input(f"enter a number between {lower_bound}-{upper_bound}"))
    return number

def print_happy_monday():
    print('Happy Monday!')

def print_im_sick_and_sad():
    print("Dayquill eric is weird")

def print_reminder(print_happy_day):
    print_happy_day()
    print("Did you remember to do zybooks?")

print_reminder(print_im_sick_and_sad)

print(print_im_sick_and_sad)

# can go out of order
print_rectangle(width=5, length=10)
print_rectangle(10, 5)

# keyword argument
print_date(6, year=2026)

get_number_within_range(10, 2)

print(globals())
