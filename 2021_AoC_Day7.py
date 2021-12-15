from pdb import set_trace as bp

# Input file 
f = r'C:\Users\brian\Documents\GitHub\2021-Advent-of-Code\2021_AoC_Day7_input.txt'

""" Get Data from Input File"""
with open(f,'r') as file:
    data = file.readline().split(',')
    for x in range(len(data)):
        data[x] = int(data[x])
    data.sort()
 
""" Test Only Data """
# data = [16,1,2,0,4,2,7,1,2,14]

""" Part 1 """
totals = []
for x in range(data[-1]):
    point_distances = []
    for i in data:
        distance_from = abs(x-i)
        point_distances.append(distance_from)
    total = sum(point_distances)
    totals.append(total)
min_value = min(totals)
min_index = totals.index(min_value)

fuel_total = 0
for i in data:
    add_fuel = abs(min_index-i)
    fuel_total = fuel_total + add_fuel

print("Fuel Needed Part-1: " + str(fuel_total))

""" Part 2 """
totals = []
for x in range(data[-1]):
    fuel_needs = []
    for i in data:
        distance_from = abs(x-i)
        fuel_needed = (distance_from+1)*(distance_from/2)
        fuel_needs.append(fuel_needed)
    total = sum(fuel_needs)
    totals.append(total)
min_value = min(totals)

print("Fuel Needed Part-2: " + str(min_value))
# bp()