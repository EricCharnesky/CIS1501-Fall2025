gradebook = {}

gradebook['Eric'] = { "Test 1" : 100, "Assignment 1" : 20 }
gradebook['Jeb'] =  { "Test 1" : 90, "Assignment 1" : 20 }

gradebook['Eric']['Test 1'] = 99

# crashes if key doesn't exist
# print(gradebook['Vivi'])

print(gradebook.get('Vivi', 'key not found'))

for name in gradebook:
    print(f'{name}: {gradebook[name]}')





numbers = [ 10, 6 , 4, 3, 9 ]

# don't modify lists while looping through them
# for number in numbers:
#     if number % 2:
#         numbers.remove(number)

# looping through a copy makes sure we don't skip
for number in numbers[:]:
    if number % 2:
        numbers.remove(number)

print(numbers)

def has_winner_by_diagonal(board):
    return board[1][1] != ' ' and ( ( board[0][0] == board[1][1] and board[2][2] == board[1][1] ) or \
        ( board[2][0] == board[1][1] and board[0][2] == board[1][1] ) )

def has_winner_by_column(board):
    for column_index in range(len(board)):
        if board[0][column_index] != ' ' and board[0][column_index] == board[1][column_index] and board[0][column_index] == board[2][column_index]:
            return True
    return False

def has_winner_by_row(board):
    for row in board:
        if row[0] != ' ' and row[0] == row[1] and row[0] == row[2]:
            return True
    return False

def has_winner(board):
    return has_winner_by_row(board) or has_winner_by_column(board) or has_winner_by_diagonal(board)

def is_tied(board):
    for row in board:
        if " " in row:
            return False
    return not has_winner(board)

def game_over(board):
    return is_tied(board) or has_winner(board)

def make_move(player, board):
    move = input(f"{player}'s turn - Enter a row and column")
    row, column = [ int(value) for value in move.split() ]
    while board[row][column] != ' ':
        print("can't go there")
        move = input(f"{player}'s turn - Enter a row and column")
        row, column = [ int(value) for value in move.split() ]
    board[int(row)][int(column)] = player


board = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]


player = 'X'
while not game_over(board):
    print("\n".join(str(row) for row in board))
    make_move(player, board)
    player = 'O' if player == 'X' else 'X'
    # if player == "X":
    #     player = 'O'
    # else:
    #     player = 'X'

print( "\n".join(str(row) for row in board) )

# for row in board:
#     print(row)

