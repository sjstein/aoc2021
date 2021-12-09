# D8P1
fname = 'input_p1'
fp = open(fname, 'r')

data = []
for line in fp:
    data.append(line.strip().split('|'))

accum = 0
outputs = []
for i in range(0, len(data)):
    outputs.append(data[i][1].split())

print(outputs)

for i in range(0, len(outputs)):
    for j in range(0, 4):
        ml = len(outputs[i][j])
        if ml == 2 or ml == 3 or ml == 4 or ml == 7:
            accum += 1
            print(f'found unique: {outputs[i][j]}, accum = {accum}')


print(f'ans: {accum}')

