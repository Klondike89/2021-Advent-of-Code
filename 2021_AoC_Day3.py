
f = r'C:\Users\brian\Documents\GitHub\2021-Advent-of-Code\2021_AoC_Day3_input.txt'

full = []

with open(f,'r') as file:
    for line in file:
        line = line.strip()
        full.append(line)

gama = ''
epsilon = ''
for pos in range(len(full[0])):
    O = 0
    I = 0
    # print(O)
    # print(I)
    # import pdb; pdb.set_trace()
    for char in range(len(full)):
        if full[char][pos] == '0':
            O += 1
        elif full[char][pos] == '1':
            I += 1
    if O > I:
        gama = gama+'0'
        epsilon = epsilon+'1'
    if I > O:
        gama = gama+'1'
        epsilon = epsilon+'0'
    # print(O)
    # print(I)
    # print(gama)
    # print(epsilon)
    # pdb.set_trace()
gama = int(gama,2)
epsilon = int(epsilon,2)
print(gama*epsilon)