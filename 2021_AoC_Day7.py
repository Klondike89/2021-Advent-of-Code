from pdb import set_trace as bp
from statistics import median

f = r'C:\Users\brian\Documents\GitHub\2021-Advent-of-Code\2021_AoC_Day7_input.txt'

with open(f,'r') as file:
    data = file.readline().split(',')
    for x in range(len(data)):
        data[x] = int(data[x])
    data.sort()

# print(data)
# print(data[len(data)-1])
# data = [16,1,2,0,4,2,7,1,2,14]

totals = []
for x in range(data[-1]):
    point_distances = []
    for i in data:
        distance_from = abs(x-i)
        point_distances.append(distance_from)
        # print(point_distances)
    total = sum(point_distances)
    totals.append(total)
min_value = min(totals)
min_index = totals.index(min_value)

fuel_total = 0
for i in data:
    add_fuel = abs(min_index-i)
    fuel_total = fuel_total + add_fuel

print(fuel_total)

# bp()