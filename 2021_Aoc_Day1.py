with open(r'C:\Users\brian\Documents\GitHub\2021-Advent-of-Code\2021_AoC_Day1_input.txt','r') as file:
    x = 0
    old_window = []
    new_window = []
    old_window.append(int(file.readline()))
    for line in range(2):
        start = int(file.readline())
        old_window.append(start)
        new_window.append(start)
    # print(old_window)
    # print(new_window)
    # import pdb; pdb.set_trace()
    for line in file:
        # print(old_window)
        # print(new_window)
        new_window.append(int(line))
        # print(old_window)
        # print(new_window)
        if sum(new_window) > sum(old_window):
            x += 1
        del old_window[0]
        del new_window[0]
        old_window.append(int(line))
        # print(old_window)
        # print(new_window)
print(x)
