import random
from random import randint

from chair import Chair

from lotto_ticket import LottoTicket


if __name__ == "__main__":
    print(__name__)

def print_chair(some_chair : Chair):
    print(f"Color: {some_chair.get_color()}")
    print(f'Current Height in cm: {some_chair.get_height_in_cm()}')
