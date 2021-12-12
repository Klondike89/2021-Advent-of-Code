import re
f = r'C:\Users\brian\Documents\GitHub\2021-Advent-of-Code\2021_AoC_Day2_input.txt'
with open(f) as file:
    x_axis = 0
    y_axis = 0
    rotation = 0
    for line in file:
        v = re.findall(r'\d$', line)
        v = int(''.join(v))
        f = re.search(r'^forward', line)
        u = re.search(r'^up', line)
        d = re.search(r'^down', line)
        if d:
            rotation += v
        elif u:
            rotation -= v
        elif f:
            y_axis += rotation*v
            x_axis += v
print(x_axis*y_axis)