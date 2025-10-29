import random

class Chair:

    # initialize or constructor
    # it's job is to give attributes names and values
    def __init__(self, color, has_arms = False, current_height = 30, minimum_height = 0, max_height = 100):
        self.set_color(color)
        # prefix with _ to 'hide' the value or make it private
        self._height_in_cm = 0
        self._minimum_height_in_cm = minimum_height
        self._maximum_height_in_cm = max_height
        self.change_height(current_height)
        self.set_has_arms(has_arms)


    # um gpt
   # write set and get functions for the attributes of this class
    # class Chair:
    #
    # # initialize or constructor
    # # it's job is to give attributes names and values
    # def __init__(self, color, has_arms, current_height, minimum_height, max_height):
    #     self.set_color(color)
    #     # prefix with _ to 'hide' the value or make it private
    #     self._height_in_cm = 0
    #     self._minimum_height_in_cm = minimum_height
    #     self._maximum_height_in_cm = max_height
    #     self.change_height(current_height)
    #     self._has_arms = has_arms

    def set_has_arms(self, has_arms):
        self._has_arms = has_arms

    def get_has_arms(self):
        return self._has_arms

    def get_minimum_height(self):
        return self._minimum_height_in_cm

    def get_maximum_height(self):
        return self._maximum_height_in_cm

    def get_height_in_cm(self):
        return self._height_in_cm

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    # protects the value of current height - keeps it in bounds
    def change_height(self, change_in_cm):
        self._height_in_cm += change_in_cm
        if self._height_in_cm > self._maximum_height_in_cm:
            self._height_in_cm = self._maximum_height_in_cm
        elif self._height_in_cm < self._minimum_height_in_cm:
            self._height_in_cm = self._minimum_height_in_cm

    # how to represent the instance as a string ( works with print )
    def __str__(self):
        return f'Color: {self._color} - Current Height: {self._height_in_cm}'


def print_chair(some_chair : Chair ):
    print(f"Color: {some_chair.get_color()}")
    print(f'Current Height in cm: {some_chair.get_height_in_cm()}')

# calls the init method
erics_chair = Chair("blue")
# python lets you do bad things
# erics_chair._height_in_cm = 700
erics_chair._has_arms = False
erics_chair._maximum_height_in_cm = 70
erics_chair._minimum_height_in_cm = 70
erics_chair.change_height(10)

jubilees_chair = Chair("orange")
jubilees_chair._has_arms = False
jubilees_chair._maximum_height_in_cm = 100
jubilees_chair._minimum_height_in_cm = 30
jubilees_chair.change_height(50)

print_chair(erics_chair)
print_chair(jubilees_chair)
print(erics_chair) # uses the __str__ method
print(jubilees_chair)



class LottoTicket:

    def __init__(self, number1, number2, number3):
        self._number1 = self._validate_number(number1)
        self._number2 = self._validate_number(number2)
        self._number3 = self._validate_number(number3)

    # private helper function
    def _validate_number(self, number):
        if 0 < number < 10:
            return number
        return 0


    def get_number_1(self):
        return self._number1

    def get_number_2(self):
        return self._number2

    def get_number_3(self):
        return self._number3

    def is_winner_regardless_of_order(self, winning_ticket):
        numbers = {self._number1, self._number2, self._number3}
        winning_numbers = {winning_ticket.get_number_1(), winning_ticket.get_number_2(), winning_ticket.get_number_3()}

        return len(numbers.intersection(winning_numbers)) == 3

    def is_winner(self, winning_ticket ):
        return self._number1 == winning_ticket.get_number_1() and \
                self._number2 == winning_ticket.get_number_2() and \
                self._number3 == winning_ticket.get_number_3()

    def __str__(self):
        return f'{self._number1} {self._number2} {self._number3}'


erics_ticket = LottoTicket(1, 2, 3)
winning_ticket = LottoTicket(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10) )
cheating_ticket = LottoTicket(1,2,3)
print(erics_ticket.is_winner(winning_ticket))
print(erics_ticket.is_winner(cheating_ticket))


did_win = False
number_of_tickets = 0
while not did_win:
    new_ticket = LottoTicket(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10) )
    did_win = new_ticket.is_winner(winning_ticket)
    print(new_ticket)
    number_of_tickets += 1

print(f"You won! it only took {number_of_tickets} tries!")
print(winning_ticket)
