# D6P2
fname = 'input_p1'
fp = open(fname, 'r')

# Instead of growing the list as the population grows, let's just keep track of how many fish of each age there are
# Fish[age][num]
fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]

school = list(map(int, fp.read().split(',')))
# Populate starting fish pool
for f in range(0, len(school)):
    fish[school[f]] += 1
print(fish)

iter = 0
while iter < 256:
    delta = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for f in range(0, len(fish)):
        if f == 0:
            if fish[0] > 0:
                delta[0] -= fish[0]
                delta[6] += fish[0]
                delta[8] += fish[0]
        elif fish[f] > 0:
            delta[f] -= fish[f]
            delta[f-1] += fish[f]
        # print(f'delta: {f} : {delta}')

    for f in range(0, len(fish)):
        fish[f] += delta[f]
    print(f'corrected fish [{iter}]: {fish}')
    iter += 1

accum = 0
for f in range(0, len(fish)):
    accum += fish[f]

print(f'answer: {accum}')