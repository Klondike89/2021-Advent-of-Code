
f = r'C:\Users\brian\Documents\GitHub\2021-Advent-of-Code\2021_AoC_Day3_input.txt'

full = []
oxy = []
co2 = []
list_one = []
list_zero = []

with open(f,'r') as file:
    for line in file:
        line = line.strip()
        if line[0] == '1':
            list_one.append(line)
        elif line[0] == '0':
            list_zero.append(line)
        full.append(line)

oxy = full.copy()
co2 = full.copy()

# for char in range(len(full)):
#     O = 0
#     I = 0
#     if full[char][0] == '0':
#         O += 1
#     elif full[char][0] == '1':
#         I += 1
# if O > I:
#     oxy = list_zero.copy()
#     co2 = list_one.copy()
# elif I > O:
#     oxy = list_one.copy()
#     co2 = list_zero.copy()


for pos in range(len(oxy[0])):
    O = 0
    I = 0
    list_zero.clear()
    list_one.clear()
    # print(oxy)
    # print(O)
    # print(I)
    # print(list_one)
    # print(list_zero)
    import pdb; #pdb.set_trace()
    for char in range(len(oxy)):
        if oxy[char][pos] == '0':
            O += 1
            list_zero.append(oxy[char])
        if oxy[char][pos] == '1':
            I += 1
            list_one.append(oxy[char])
        # print(list_one)# test list one and zero append
        # print(list_zero)# test list one and zero append
        # pdb.set_trace()# test list one and zero append
    oxy.clear()
    if O > I:
        oxy = list_zero.copy()
        # print("O's win. Spot: "+str(pos))
        if len(oxy)==1:
            break
    elif I > O:
        oxy = list_one.copy()
        # print("I's win. Spot: "+str(pos))
        if len(oxy)==1:
            break
    elif I == O:
        oxy = list_one.copy()
        # print("Its a tie take 1. Spot: "+str(pos))
        if len(oxy)==1:
            break
    # pdb.set_trace()

for pos in range(len(co2[0])):
    O = 0
    I = 0
    list_zero.clear()
    list_one.clear()
    # print(co2)
    # print(O)
    # print(I)
    # print(list_one)
    # print(list_zero)
    import pdb; #pdb.set_trace()
    for char in range(len(co2)):
        if co2[char][pos] == '0':
            O += 1
            list_zero.append(co2[char])
        if co2[char][pos] == '1':
            I += 1
            list_one.append(co2[char])
        # print(list_one)# test list one and zero append
        # print(list_zero)# test list one and zero append
        # pdb.set_trace()# test list one and zero append
    co2.clear()
    if O > I:
        co2 = list_one.copy()
        # print("O's win. Spot: "+str(pos))
        if len(co2)==1:
            break
    elif I > O:
        co2 = list_zero.copy()
        # print("I's win. Spot: "+str(pos))
        if len(co2)==1:
            break
    elif I == O:
        co2 = list_zero.copy()
        # print("Its a tie take 1. Spot: "+str(pos))
        if len(co2)==1:
            break
   

print("Final Oxy: " + oxy[0])
print("Final Co2: " + co2[0])
oxygen = int(oxy[0],2)
carbon = int(co2[0],2)
print(oxygen)
print(carbon)
print(oxygen*carbon)