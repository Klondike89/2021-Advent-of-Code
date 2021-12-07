from pdb import set_trace as bp

f = r'C:\Users\brian\Documents\GitHub\2021-Advent-of-Code\2021_AoC_Day4_input.txt'

board_line = int(1)
board = []
all_boards = []
column = []

vert_count = 0
horz_count = 0
found = False

def create_board(name):
    name = board.copy()
    all_boards.append(name)
    board.clear()

with open(f,'r') as file:
    called_numbers = file.readline().strip()
    called_numbers = called_numbers.split(',')
    for line in file:
        if line != '\n':
           board.append(line.split())
        else:
            if board != all_boards:
                create_board(line)

def mark_called(value,num):
    if value == num:
        # board[char][pos] = 'XX' ### TAKE THIS OUT!
        board[char][pos] = value+'c'#### PUT THIS BACK IN
    column.append(board[char][pos])

winner = []
last_call = 0
for num in called_numbers:
    last_call = int(num)
    for board in all_boards:
        for pos in range(len(board[0])):
            column.clear()
            for char in range(len(board)):
                value = board[char][pos]
                
                mark_called(value,num)

                if len(column) == len(board):
                    vert_count = 0
                    for space in column:
                        if space.isdigit():
                            pass
                        else:
                            vert_count += 1
                            if vert_count == len(board):
                                for line in board:
                                    winner.append(line)
                                #     print(line)
                                # print("Bingo!")
                                found = True
                    for line in board:
                        horz_count = 0
                        for space in line:
                            if space.isdigit():
                                pass
                            else:
                                horz_count += 1
                                if horz_count == len(board):
                                    winner.append(board)
                                    # print(board)
                                    # print("BINGO!")
                                    found = True
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
for line in winner:
    for spot in line:
        if spot.isdigit():
            uncalled_spots.append(int(spot))
        
print(sum(uncalled_spots)* last_call)