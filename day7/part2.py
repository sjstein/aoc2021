# D7P2

fname = 'input_p1'
fp = open(fname, 'r')


# from functools import lru_cache
#
#
# @lru_cache(maxsize=None)
# def fuel(n):
#     if n < 2:
#         return n
#     else:
#         return n + fuel_memo(n-1)



def fuel(n):
    a = 0
    for y in range(1, n+1):
        a += y
    return a


crabpos = list(map(int, fp.read().split(',')))

print(crabpos)
accum = []
for i in range(0, max(crabpos)):
    inaccum = 0
    for j in range(0, len(crabpos)):
        fcons = fuel(abs(crabpos[j] - i))
        #print(f'Looking at fuel between {crabpos[j]} and {i} = {fcons}')
        inaccum += fcons
    accum.append(inaccum)

print(accum)
print(min(accum))

# Too high: 93009400
