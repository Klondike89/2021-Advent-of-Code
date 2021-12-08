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
num_index = 0
found_first = False
found_all = False
found_any = False

def is_win_case(board):
    i = 0
    while i <= 20:
        if sum([board[i],board[i+1],board[i+2],board[i+3],board[i+4]]) == 500:
            return True
        i += 5
    i = 0
    while i <= 4:
        if sum([board[i],board[i+5],board[i+10],board[i+15],board[i+20]]) == 500:
            return True
        i += 1


def update_boards(board):
        if num in board:
            x = board.index(num)
            board[x] = 100

def board_total(board):
    larry = [x for x in board if x != 100]
    print(larry)
    print(num)
    total = sum(larry)*num
    print(total)

while not found_all:
    num = called_numbers[num_index]
    b_index_count = 0
    # print('num: ' + str(num_index))
    # print('len: ' + str(len(winners)))
    # print('winners: ' + str(board_indexes))
    for b_index_count in board_indexes:
        board = boards[int(b_index_count)]
        update_boards(board)
        
        if is_win_case(board):
            board_indexes.remove(b_index_count)
            if not found_first:
                board_total(board)
                found_first = True
            
            elif len(board_indexes) == 0 or len(board_indexes) < 5:
                print(num)
                print(b_index_count)
                print(board_indexes)
                for x in range(0,5):
                    x = x*5
                    print(board[x:x+5])
                board_total(board)
                #found_all = True
            b_index_count -= 1    
            #bp()
        b_index_count += 1
    num_index += 1
                