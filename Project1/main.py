import random
from tarfile import ExtractError


def menu():
    valid_choices = ("x-", "x+", "y-", "y+", "thrusters", "nothing", "self destruct")
    choice = ""

    while choice not in valid_choices:
        choice = input(f"Enter a choice: {valid_choices}")

    return choice

def print_landed_message(xTilt, yTilt):
    # if xTilt != 0 or yTilt != 0
    if xTilt or yTilt:
        print("You crashed, there goes our billion dollar lander!")
    else:
        print("You landed safely")

SELF_DESTRUCT_CANCELLATION_CODE = '00000'


play_again = 'y'

while play_again == 'y':

    xTilt = random.randint(-10, 10)
    yTilt = random.randint(-10, 10)

    self_destruct_activated = False

    distance_from_surface = 10

    while distance_from_surface > 0:
        print(f'X Tilt: {xTilt}, Y Tilt: {yTilt}, Distance from surface: {distance_from_surface}')

        if self_destruct_activated:
            code = input("Enter self destruct cancellation code")
            if code == SELF_DESTRUCT_CANCELLATION_CODE:
                self_destruct_activated = False
                print("Deactivated self destruct")
            else:
                print("Invalid code!!!!")
        else:
            choice = menu()

            if choice == "x-":
                xTilt -= 1
            elif choice == "x+":
                xTilt += 1
            elif choice == "y-":
                yTilt -= 1
            elif choice == "y+":
                yTilt += 1
            elif choice == "thrusters":
                distance_from_surface += 2
            elif choice == "nothing":
                pass
            elif choice == "self destruct":
                self_destruct_activated = True
                pass

        distance_from_surface -= 1

    print_landed_message(xTilt, yTilt)

    play_again = input("Do you want to play again? y/n")
