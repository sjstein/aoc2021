# D3P1

fname = 'input_p1'
fp = open(fname, 'r')
diag = fp.read().split('\n')
result = []
gam = []
eps = []

# Create gamma and epsilon lists
for i in range(0, len(diag[0])):
    gam.append('0')
    eps.append('0')

print(f'Found {len(diag)} lines of diagnostics')
print(f'Initial lists: gamma ({gam}) and epsilon ({eps})')
for i in range(0, len(diag[0])):
    result.append(0)
    for bit in diag:
        if bit[i] == '1':
            result[i] += 1
    print(f'Scanned bit position {i} and found {result[i]} ones')
    if result[i] > len(diag) / 2:
        gam[i] = '1'
    else:
        eps[i] = '1'
    print(f'Stats: {result}, {gam}, {eps}')

print(f'result list = {result}, gam list = {gam}, eps list = {eps}')
bgam = bin(int(''.join(gam), 2))
beps = bin(int(''.join(eps), 2))
igam = int(bgam, 2)
ieps = int(beps, 2)
print(f'Results: gamma ({bgam}) = {igam}, epsilon ({beps}) = {ieps}, answer: {igam * ieps}')
