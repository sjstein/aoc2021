# D1P1

fname = 'input_p1'
fp = open(fname, 'r')
depths = fp.read().split()
depths = list(map(int, depths))  # Cast list elements to ints

inc = 0     # Counter for each time a depth increases from one element to the next in the series
for num in range(0, len(depths)):
    if num + 3 > len(depths) - 1:
        break
    win1 = depths[num] + depths[num + 1] + depths[num + 2]
    win2 = depths[num + 1] + depths[num + 2] + depths[num + 3]
    if win2 > win1:
        inc += 1

print(f'result={inc}')