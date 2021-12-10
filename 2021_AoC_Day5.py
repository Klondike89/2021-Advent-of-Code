from pdb import set_trace as bp

f = r'C:\Users\brian\Documents\GitHub\2021-Advent-of-Code\2021_AoC_Day5_input.txt'

""" X1,Y1 -> X2,Y2 """
cord_lines = []
drawn_lines = {}

with open(f,'r') as file:
    for line in file:
        cord1 = line.strip().split(' -> ')[0]
        cord2 = line.strip().split(' -> ')[1]

        cord1 = [int(x)for x in cord1.split(',')]
        cord2 = [int(x)for x in cord2.split(',')]
        cord_lines.append(tuple([tuple(cord1),tuple(cord2)]))

def draw_line(cord):
    if cord not in drawn_lines:
        drawn_lines[cord] = 0
    else:
        drawn_lines[cord] += 1

for line_set in cord_lines:
    start_x = line_set[0][0]
    start_y = line_set[0][1]
    stop_x = line_set[1][0]
    stop_y = line_set[1][1]

        ### Vertical ###
    if start_x == stop_x:
        for i in range(start_y,stop_y+1):
            draw_line(str(start_x)+','+str(i))
        for i in range(stop_y,start_y+1):
            draw_line(str(start_x)+','+str(i))


        ### Horizontal ###
    if start_y == stop_y:
        for i in range(start_x,stop_x+1):
            draw_line(str(i)+','+str(start_y))
        for i in range(stop_x,start_x+1):
            draw_line(str(i)+','+str(start_y))

points = [x for x in drawn_lines.values() if x>0]
print('Number of Overlaps: ' + str(len(points)))