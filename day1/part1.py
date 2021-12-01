# D1P1

fname = 'input_p1'
fp = open(fname, 'r')
col = fp.read().split()

inc = 0
print(col)
for num in range(1, len(col)):
    if col[num] > col[num-1]:
        inc += 1
        print(f'comp# {num} : {col[num]} > {col[num - 1]}? YES (inc = {inc})')
    else:
        print(f'comp# {num} : {col[num]} > {col[num - 1]}? NO  (inc = {inc})')

print(f'result={inc}')