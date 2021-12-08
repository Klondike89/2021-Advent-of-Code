from pdb import set_trace as bp

f = r'C:\Users\brian\Documents\GitHub\2021-Advent-of-Code\2021_AoC_Day4_input.txt'

with open(f,'r') as file:
    called_numbers = [int(x) for x in file.readline().strip().split(',')]
    boards = []
    while file.readline():
        board = []
        for i in range(5):
            board.extend([int(x) for x in file.readline().strip().split(' ') if x != ('')])
        boards.append(board)

board_indexes = [x for x in range(len(boards))]
winners = []
found_first = False
found_all = False
found_any = False

""" Update board by replacing drawn number with '100' """
def update_boards(board):
        if num in board:
            x = board.index(num)
            board[x] = 100

""" Calculate total value of all uncalled values on board then multiply by drawn number """
def board_total(board):
    larry = [x for x in board if x != 100]
    for x in range(5):
        x = x*5
        print(board[x:x+5])
    print(larry)
    print(num)
    total = sum(larry)*num
    print(total)

""" Define what a win looks like """
def is_win_case(board):
    i = 0
    while i <= 20:
        if sum([board[i],board[i+1],board[i+2],board[i+3],board[i+4]]) == 500:
            board_total(board)
            return True
        i += 5
    i = 0
    while i <= 4:
        if sum([board[i],board[i+5],board[i+10],board[i+15],board[i+20]]) == 500:
            board_total(board)
            return True
        i += 1

while found_all == False:
    num = called_numbers[0]
    called_numbers = called_numbers[1:]
    for index in range(len(boards)):
        board = boards[index]
        update_boards(board)
    play_index = 0
    while play_index < len(boards):
        # print(len(boards))
        # print(boards)
        if is_win_case(boards[play_index]):
            if len(boards) > 1:
                boards.pop(play_index)
            else:
                found_all = True
                play_index += 1
            #bp()
        else:
            play_index += 1
    print(len(boards))
    #bp()

print(boards)