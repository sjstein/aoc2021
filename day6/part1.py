# D6P1
fname = 'input_p1'
fp = open(fname, 'r')

school = list(map(int, fp.read().split(',')))
iter = 0
# while iter < 80:
#     for fish in school:
#         print(f'checking fish: {fish}')
#         if fish == 0:
#             fish = 6
#             school.append(8)
#         else:
#             fish -= 1
#             print(f'growing fish: {fish}')
#
#     print(f'SchoolState: {school}')
#     iter += 1
# print(f'done with iter= {iter} and school size = {len(school)}')

while iter < 80:
    for f in range(0, len(school)):
        if school[f] == 0:
            school[f] = 6
            school.append(8)
        else:
            school[f] -= 1
    print(f'school [{iter}]: {school}')
    iter += 1

print(f'done with iter= {iter} and school size = {len(school)}')
