import random

class LottoTicket:

    def __init__(self, number1, number2, number3):
        self._number1 = self._validate_number(number1)
        self._number2 = self._validate_number(number2)
        self._number3 = self._validate_number(number3)

    # private helper function
    def _validate_number(self, number):
        if 0 < number < 10:
            return number
        raise ValueError("Number must be 1-9")


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


if __name__ == "__main__":

    erics_ticket = LottoTicket(1, 2, 3)
    winning_ticket = LottoTicket(random.randint(1, 9), random.randint(1, 9), random.randint(1, 9) )
    cheating_ticket = LottoTicket(1,2,3)
    print(erics_ticket.is_winner(winning_ticket))
    print(erics_ticket.is_winner(cheating_ticket))


    did_win = False
    number_of_tickets = 0
    while not did_win:
        new_ticket = LottoTicket(random.randint(1, 9), random.randint(1, 9), random.randint(1, 9) )
        did_win = new_ticket.is_winner(winning_ticket)
        print(new_ticket)
        number_of_tickets += 1

    print(f"You won! it only took {number_of_tickets} tries!")
    print(winning_ticket)
