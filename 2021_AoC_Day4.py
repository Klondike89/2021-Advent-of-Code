from pdb import set_trace as bp

f = r'C:\Users\brian\Documents\GitHub\2021-Advent-of-Code\2021_AoC_Day4_input.txt'

board_line = int(1)
a = []
b = []
c = []
d = []
e = []
all_boards = []

def build_board(board_line):
    if board_line == 1:
        a.append(line.split(' '))
    elif board_line == 2:
        b.append(line.split(' '))
    elif board_line == 3:
        c.append(line.split(' '))
    elif board_line == 4:
        d.append(line.split(' '))
    elif board_line == 5:
        e.append(line.split(' '))

def create_board(name):
    name = [a.copy(),b.copy(),c.copy(),d.copy(),e.copy()]
    all_boards.append(name)

def clear_lines():
    a.clear()
    b.clear()
    c.clear()
    d.clear()
    e.clear()

with open(f,'r') as file:
    called_numbers = file.readline()
    for line in file:
        # print(all_boards); print(board_line); print(line); bp()
        if line != '\n':
            line = line.strip('\n')
            build_board(board_line)
            board_line +=1
            # print(all_boards); print(board_line); print(line); bp()
        else:
            if a != all_boards:
                board_line = int(1)
                create_board(line)
                clear_lines()
                # print(all_boards); print(board_line); print(line); bp()


for board in all_boards:
    print(board)