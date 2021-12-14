from pdb import set_trace as bp
from statistics import median
f = r'C:\Users\brian\Documents\GitHub\2021-Advent-of-Code\2021_AoC_Day7_input.txt'

with open(f,'r') as file:
    data = file.readline().split(',')
    for x in range(len(data)):
        data[x] = int(data[x])
    data.sort()

found = False

set_top = len(data)-1
set_bottom = data[0]
set_center = int(median(data))

def find_mid_point(point1,point2):
    mid_point = int(median([point1,point2]))
    return mid_point


def test_vs_high(test_high_point):
    for i in data:
        if i > test_high_point:
            high_total = high_total + (i - test_high_point)
        if i < test_high_point:
            high_total = high_total + (test_high_point - i)
    return high_total

def test_vs_low(test_low_point):
    for i in data:
        if i > test_low_point:
            low_total = low_total + (i - test_low_point)
        if i < test_low_point:
            low_total = low_total + (test_low_point - i)
    return low_total

def test_found(low_total, high_total):
    if low_total == high_total:
        found = True



while not found:

    print('High_total: ' + str(high_total))
    print('Low_total: ' + str(low_total))
    print('Bottom: '+ str(set_bottom))
    print('Center: '+ str(set_center))
    print('Top: '+ str(set_top))

    test_high_point = find_mid_point(set_center,set_top)
    test_low_point = find_mid_point(set_center, set_bottom)
    test_found(
        test_vs_high(test_high_point),
        test_vs_low(test_low_point)
        )

    if low_total < high_total:
        set_top = set_center
        set_center = test_low_point
    
    elif low_total > high_total:
        set_bottom = set_center
        set_center = test_high_point
    
    bp()

    

