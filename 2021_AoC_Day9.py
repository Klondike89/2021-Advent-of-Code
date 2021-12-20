from pdb import set_trace as bp
# Input file 
f = r'C:\Users\brian\Documents\GitHub\2021-Advent-of-Code\2021_AoC_Day9_input.txt'

risk_level_total = 0

##--- Get Data from Input File ---##
with open(f,'r') as file:
    data = [tuple(int(x) for x in line.strip()) for line in file]


cords = [(column,row) for row in range(len(data)) for column in range(len(data[0]))]
# print(data)
# print(cords)
# print(len(data))
# print(len(data[0]))

for cord in cords:
    x = cord[1]
    y = cord[0]
    value = data[x][y]
    comparison_cords = {(y,x+1),
                        (y,x-1),
                        (y+1,x),
                        (y-1,x)
                            }
    # print(cord)
    
    bad_cord_lst = []
    for adj_cord in comparison_cords:
        if adj_cord[0] < 0 or adj_cord[1] < 0:
            bad_cord_lst.append(adj_cord)
        elif  adj_cord[1] > len(data)-1:
            bad_cord_lst.append(adj_cord)
        elif adj_cord[0] > len(data[0])-1 or adj_cord[1] > len(data[0])-1:
            bad_cord_lst.append(adj_cord)
    for bad_cord in bad_cord_lst:
        comparison_cords.remove(bad_cord)
    # print(comparison_cords)
    is_lowest = False
    if len(comparison_cords) != 0:
        is_lowest = True
    
        for adj_cord in comparison_cords:
            # print(adj_cord)
            adj_x = adj_cord[1]
            adj_y = adj_cord[0]
            # print(data[adj_x][adj_y])
            adj_value = data[adj_x][adj_y]
            if value >= adj_value:
                # print('Number: ' + str(value) + ' Is NOT Less Than: ' + str(adj_value))
                is_lowest = False
                break
            # else:
            #     print('Number: ' + str(value) + ' Is Less Than: ' + str(adj_value))
    if is_lowest:        
        # print(str(cord) +' WINNER!!!!!!!!!!  Number: ' + str(value) + ' Is Less Than: ' + str(adj_value))
        # for adj_cord in comparison_cords:
        #     print(adj_cord)
        #     adj_x = adj_cord[1]
        #     adj_y = adj_cord[0]
        #     print(data[adj_x][adj_y])
        #     adj_value = data[adj_x][adj_y]
        #     if value > adj_value:
        #         print('Number: ' + str(value) + ' Is NOT Less Than: ' + str(adj_value))
        #         is_lowest = False
        #         break
        #     else:
        #         print('Number: ' + str(value) + ' Is Less Than: ' + str(adj_value))
        risk_level_total = risk_level_total + value + 1

print('Risk Level: '+str(risk_level_total))
    