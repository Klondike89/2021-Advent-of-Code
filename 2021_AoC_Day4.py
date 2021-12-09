from pdb import set_trace as bp

f = r'C:\Users\brian\Documents\GitHub\2021-Advent-of-Code\2021_AoC_Day4_input.txt'

board_line = int(1)
board = []
all_boards = []
column = []

vert_count = 0
horz_count = 0
found = False

""" Define How to Build Boards and then add Board to list of All_Boards """
def create_board(name):
    name = board.copy()
    all_boards.append(name)
    board.clear()

""" Open File and create needed lists """
with open(f,'r') as file:
    called_numbers = file.readline().strip()
    called_numbers = called_numbers.split(',')
    for line in file:
        if line != '\n':
           board.append(line.split())
        else:
            if board != all_boards:
                create_board(line)

""" How to mark spots on board as called """
def mark_called(value,num):
    if value == num:
        board[char][pos] = value+'c'
    column.append(board[char][pos])

winner = []
last_call = 0
# Call a number
for num in called_numbers:
    last_call = int(num)
# Go through each Board
    for board in all_boards:
# Iterate through board going down through each column
        for pos in range(len(board[0])):
            column.clear()
            for char in range(len(board)):
                value = board[char][pos]
# Mark values if qualify               
                mark_called(value,num)
# Check columns for win case
                if len(column) == len(board):
                    vert_count = 0
                    for space in column:
                        if space.isdigit():
                            pass
                        else:
                            vert_count += 1
                            if vert_count == len(board):
                                winner.append(board)
                                found = True
# Check lines for win case
                    for line in board:
                        horz_count = 0
                        for space in line:
                            if space.isdigit():
                                pass
                            else:
                                horz_count += 1
                                if horz_count == len(board):
                                    winner.append(board)
                                    found = True
# Break out of all loops when finished
                    if found == True:
                        break
                if found == True:
                    break
            if found == True:
                break
        if found == True:
            break
    if found == True:
        break


uncalled_spots = []

for win in winner:
    for pos in range(len(win[0])):
        for spot in range(len(win)):
            square = win[spot][pos]
            if square.isdigit():
                uncalled_spots.append(int(square))
      
print(sum(uncalled_spots)* last_call)