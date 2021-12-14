from pdb import set_trace as bp
from statistics import median
f = r'C:\Users\brian\Documents\GitHub\2021-Advent-of-Code\2021_AoC_Day7_input.txt'

with open(f,'r') as file:
    data = file.readline().split(',')
    for x in range(len(data)):
        data[x] = int(data[x])
    data.sort()

found = False

set_points = [data[0],int(median(data)),len(data)-1]
set_bottom = set_points[0]
set_center = set_points[1]
set_top = set_points[2]

def find_mid_point(point1,point2):
    mid_point = int(median([point1,point2]))
    return mid_point


def test_vs_high(test_high_point):
    high_total = 0
    for i in data:
        if i > test_high_point:
            high_total = high_total + (i - test_high_point)
        if i < test_high_point:
            high_total = high_total + (test_high_point - i)
    print('High_total: ' + str(high_total))
    return high_total

def test_vs_low(test_low_point):
    low_total = 0
    for i in data:
        if i > test_low_point:
            low_total = low_total + (i - test_low_point)
        if i < test_low_point:
            low_total = low_total + (test_low_point - i)
    print('Low_total: ' + str(low_total))
    return low_total

def test_found(low_total, high_total):
    if low_total == high_total:
        found = True
        return found
    else:
        return low_total, high_total

def new_set(low_total, high_total):
    if low_total < high_total:
        set_points[2] = set_points[1]
        set_points[1] = test_low_point
    
    elif low_total > high_total:
        set_points[0] = set_points[1]
        set_points[1] = test_high_point



while not found:
    
    print('Bottom: '+ str(set_points[0]))
    print('Center: '+ str(set_points[1]))
    print('Top: '+ str(set_points[2]))

    test_high_point = find_mid_point(set_center,set_top)
    test_low_point = find_mid_point(set_center, set_bottom)
    new_set(
        test_vs_low(test_low_point),
        test_vs_high(test_high_point)
        )

    
    
    bp()

    

