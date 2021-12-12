
f = r'C:\Users\brian\Documents\GitHub\2021-Advent-of-Code\2021_AoC_Day6_input.txt'

ages = [x for x in range(0,9)]
current_generation = {}
for age in ages:
    current_generation[age] = 0

with open(f,'r') as file:
    data = file.readline().split(',')
    for fish in data:
        current_generation[int(fish)] += 1

Days_Observed = int(256)

last_key = 0
for day in range(Days_Observed):
    add_value = 0
    for key in range(9):
        if key != 0:
            current_generation[last_key] = current_generation.get(key)
            if key == 7:
                saved_six = current_generation.get(key)
        
        elif key == 0:
            add_value = current_generation.get(key)

        last_key = key
    current_generation[6] = saved_six + add_value
    current_generation[8] = add_value

total_count = 0
for key in range(9):
    total_count = total_count + current_generation.get(key)

print('Total Count: ' + str(total_count))