
def get_word():
    word = ""
    while len(word) < 4:
        word = input("Enter a 4 character or longer word")
    return word


def has_the_word_been_guessed(hidden_word, letters_guessed):
    for letter in hidden_word:
        if letter not in letters_guessed:
            return False
    return True


def has_person_been_hanged(number_of_incorrect_guesses):
    return number_of_incorrect_guesses >= 6


def display_hidden_word(hidden_word, letters_guessed):
    for letter in hidden_word:
        if letter in letters_guessed:
            print(letter, end=" ")
        else:
            print("_", end=" ")

def get_letter_guess(letters_guessed):
    guess = ""
    while len(guess) != 1 or guess in letters_guessed:
        guess = input("Enter a single letter to guess")
        if guess in letters_guessed:
            print("You already guessed that")
    letters_guessed.append(guess)
    return guess

def is_letter_guessed_in_hidden_word(guess, hidden_word):
    return guess in hidden_word

def print_gallows(number_of_incorrect_guesses):
    if number_of_incorrect_guesses == 0:
        print("""
| -----
|    |
|    
|  
|  
|
-----------
""")
    elif number_of_incorrect_guesses == 1:
        print("""
| -----
|    |
|    O
|  
|   
|
-----------
""")
    elif number_of_incorrect_guesses == 2:
        print("""
| -----
|    |
|    O
|    |
|   
|
-----------
""")
    elif number_of_incorrect_guesses == 3:
        print("""
| -----
|    |
|    O
|  --|
|   
|
-----------
""")
    elif number_of_incorrect_guesses == 4:
        print("""
| -----
|    |
|    O
|  --|--
|   
|
-----------
""")
    elif number_of_incorrect_guesses== 5:
        print("""
| -----
|    |
|    O
|  --|--
|   /
|
-----------
""")
    elif number_of_incorrect_guesses == 6:
        print("""
| -----
|    |
|    O
|  --|--
|   /\\
|
-----------
""")


letters_guessed = []
hidden_word = get_word()
number_of_incorrect_guesses = 0

while (not has_the_word_been_guessed(hidden_word, letters_guessed)
       and not has_person_been_hanged(number_of_incorrect_guesses)):
    display_hidden_word(hidden_word, letters_guessed)
    guess = get_letter_guess(letters_guessed)

    if not is_letter_guessed_in_hidden_word(guess, hidden_word):
        number_of_incorrect_guesses += 1

    print_gallows(number_of_incorrect_guesses)



