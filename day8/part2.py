# D8P2
fname = 'input_p1'
fp = open(fname, 'r')

# Numbers as segments:
# 0 abcefg  (6)
# 1 cf      (2)*
# 2 acdeg   (5)
# 3 acdfg   (5)
# 4 bcdf    (4)*
# 5 abdfg   (5)
# 6 abdefg  (6)
# 7 acf     (3)*
# 8 abcdefg (7)*
# 9 abcdfg  (6)
#
# breaking it down in terms of which numbers share same segments:
# a : 0,2,3,5,6,7,8,9
# b : 0,4,5,6,8,9
# c : 1,2,3,4,7,8,9
# d : 2,3,4,5,6,8,9
# e : 0,2,6,8
# f : 0,1,3,4,5,6,7,8,9
# g : 0,2,3,5,6,8,9
#

# Find a 3 from unique 7 (5 characters)
# Find a 9 from unique 4 (6 characters)
# Find a 0 from unique 8 (subset - 6 characters)
# 6 is the last 6 character digit not assigned
# 2 is inside a 6 (5 characters)
# 5 ia inside a 9 (5 characters)






data = []
for line in fp:
    data.append(line.strip().split('|'))

accum = 0
outputs = []
inputs = []

def findpat(inlist, l):
    for i in range(0, len(inlist)):
        if len(inlist[i]) == l:
            return i
    return 0

def charsInString(c, s):

    for i in range(0, len(c)):
        if not c[i] in s:
            return False
    return True

def retKey(d, s):
    for x in range(0, len(d)):
        if len(d[x]) == len(s):     # Only compare same lengths to avoid substrings
            if charsInString(s, d[x]):
                return x
    return -1



m = {}

for i in range(0, len(data)):
    outputs.append(data[i][1].split())

for i in range(0, len(data)):
    inputs.append(data[i][0].split())

print(inputs)
uniques = [2, 3, 4, 7]
unums = [1, 7, 4, 8]
solves = []


for i in range(0, len(inputs)):
    for j in range(0, len(inputs[i])):       # low hanging fruit first
        ml = len(inputs[i][j])
        ic = 0
        for n in uniques:
            if ml == n:
                #print(f'found a unique {n} input: {inputs[i][j]} corresponding to number {unums[ic]}')
                m[unums[ic]] = inputs[i][j]
            ic += 1
    solves.append(m.copy())
    #print(m)
    m.clear()
    # Now we have a dict with the easy solves filled in
    # Lets find the two other entries that have the 7 pattern
print(inputs)

for i in range(0, len(inputs)):
    # Find a 3 from unique 7 (5 characters)
    for j in range(0, len(inputs[i])):
        if len(inputs[i][j]) == 5 and charsInString(solves[i][7], inputs[i][j]) and \
                inputs[i][j] not in solves[i].values():
            solves[i][3] = inputs[i][j]
    # Find a 9 from unique 4 (6 characters)
    for j in range(0, len(inputs[i])):
        if len(inputs[i][j]) == 6 and charsInString(solves[i][4], inputs[i][j]) and \
                inputs[i][j] not in solves[i].values():
            solves[i][9] = inputs[i][j]
    # 5 is inside a 9 (5 characters) and is not a 3
    for j in range(0, len(inputs[i])):
        if len(inputs[i][j]) == 5 and charsInString(inputs[i][j], solves[i][9]) and \
                inputs[i][j] not in solves[i].values():
            solves[i][5] = inputs[i][j]
    # 2 is last 5 character remaining
    for j in range(0, len(inputs[i])):
        if len(inputs[i][j]) == 5:
            if inputs[i][j] not in solves[i].values():
                solves[i][2] = inputs[i][j]
    # Find a 0 from unique 1 (6 characters) and not a 9
    for j in range(0, len(inputs[i])):
        if len(inputs[i][j]) == 6 and charsInString(solves[i][1], inputs[i][j]) and \
                inputs[i][j] not in solves[i].values():
            solves[i][0] = inputs[i][j]
    # 6 is the last 6 character digit not assigned
    for j in range(0, len(inputs[i])):
        if len(inputs[i][j]) == 6:
            if inputs[i][j] not in solves[i].values():
                solves[i][6] = inputs[i][j]



    print('------')
    print(inputs[i])
    print(solves[i])
    print('------')



    # So at this point, the list of dictionaries (solves) contains a mapping of the segments for each digit
    # Now we need to look at the output on each line and generate the number displayed

for i in range(0, len(solves)):
    print(f'solve i len: {len(solves[i])}')

accum = 0
for i in range(0, len(outputs)):
    digits = 1000*retKey(solves[i], outputs[i][0])
    digits += 100*retKey(solves[i], outputs[i][1])
    digits += 10*retKey(solves[i], outputs[i][2])
    digits += retKey(solves[i], outputs[i][3])
    print(digits)
    accum += digits
print(f'total: {accum}')
