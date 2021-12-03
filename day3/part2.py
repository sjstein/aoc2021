# D3P2

fname = 'input_p1'
fp = open(fname, 'r')
diag = fp.read().split('\n')
result = []
gam = []
eps = []
interim = []


def checkList(loc_list, pos, type):

    # This function will take in a list of binary words
    # along with a bit position. It will return a subset list of binary words which
    # is based on the type string. If "oxy", then return subset of most frequent values,
    # if "co2", then return subset based on least frequent values

    loc_res = 0
    ret_list = []

    for loc_bit in loc_list:
        if loc_bit[pos] == '1':
            loc_res += 1

    if type == "oxy":
        if loc_res >= len(loc_list) / 2:
            for loc_bit in loc_list:
                if loc_bit[pos] == '1':
                    ret_list.append(loc_bit)
        else:
            for loc_bit in loc_list:
                if loc_bit[pos] == '0':
                    ret_list.append(loc_bit)

    else:
        if loc_res < len(loc_list) / 2:
            for loc_bit in loc_list:
                if loc_bit[pos] == '1':
                    ret_list.append(loc_bit)
        else:
            for loc_bit in loc_list:
                if loc_bit[pos] == '0':
                    ret_list.append(loc_bit)

    return ret_list



interim = diag
print(f'Found {len(diag)} lines of diagnostics')
oxylist = diag
for i in range(0, len(diag[0])):
    oxylist = checkList(oxylist, i, 'oxy')
    if len(oxylist) <= 1:
        break
    print(f'iteration {i}, list = {oxylist}')
print(f'Oxy list: {oxylist}')

co2list = diag
for i in range(0, len(diag[0])):
    co2list = checkList(co2list, i, 'co2')
    if len(co2list) <= 1:
        break
    print(f'iteration {i}, list = {co2list}')
print(f'CO2 list: {co2list}')

boxy = bin(int(oxylist[0], 2))
bco2 = bin(int(co2list[0], 2))
ioxy = int(boxy, 2)
ico2 = int(bco2, 2)

print(f'oxy: {boxy}, {ioxy}; co2: {bco2}, {ico2}; product: {ioxy * ico2}')
