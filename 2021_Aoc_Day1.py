with open(r'C:\Users\brian\Documents\GitHub\2021-Advent-of-Code\2021_AoC_Day1_input.txt','r') as file:
    x = 0
    old_line = file.readline()
    print(old_line)
    #import pdb; pdb.set_trace()
    for line in file:
        if int(line) > int(old_line):
            x += 1
        old_line = line
print(x)
