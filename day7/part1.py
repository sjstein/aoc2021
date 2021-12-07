# D7P1
fname = 'input_p1'
fp = open(fname, 'r')

crabpos = list(map(int, fp.read().split(',')))
print(crabpos)
accum = []
for i in range(0, len(crabpos)):
    inaccum = 0
    for j in range(0, len(crabpos)):
        inaccum += abs(crabpos[i] - crabpos[j])
    accum.append(inaccum)


print(min(accum))
