import re
f = r'C:\Users\brian\Documents\GitHub\2021-Advent-of-Code\2021_AoC_Day2_input.txt'
with open(f) as file:
    x = 0
    y = 0
    r = 0
    for line in file:
        v = re.findall(r'\d$', line)
        v = int(''.join(v))
        f = re.search(r'^forward', line)
        u = re.search(r'^up', line)
        d = re.search(r'^down', line)
        if d:
            r += v
        elif u:
            r -= v
        elif f:
            y += r*v
            x += v
print(x*y)