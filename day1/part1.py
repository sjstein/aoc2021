# D1P1

fname = 'input_p1'
fp = open(fname, 'r')
depths = fp.read().split()

inc = 0     # Counter for each time a depth increases from one element to the next in the series
for num in range(1, len(depths)):
    if int(depths[num]) > int(depths[num-1]):
        inc += 1
        print(f'comp# {num} : {depths[num]} > {depths[num - 1]}? YES (inc = {inc})')
    else:
        print(f'comp# {num} : {depths[num]} > {depths[num - 1]}? NO  (inc = {inc})')

print(f'result={inc}')