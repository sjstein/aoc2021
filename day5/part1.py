# D5P1
fname = 'test_in'
fp = open(fname, 'r')

coords1 = []
coords2 = []
max_x = 0
max_y = 0


def printMap(wrl):
    for i in range(0, len(wrl)):
        print(''.join(list(map(str, wrl[i]))))
    return


# Populate list of coordinates
for line in fp:
   temp = line.strip().split('->')
   coords1.append(list(map(int, temp[0].split(','))))
   coords2.append(list(map(int, temp[1].split(','))))

# Determine size of world
for i in range(0, len(coords1)):
    if coords1[i][0] > max_x:
        max_x = coords1[i][0]
    if coords1[i][1] > max_y:
        max_y = coords1[i][1]

for i in range(0, len(coords2)):
    if coords2[i][0] > max_x:
        max_x = coords2[i][0]
    if coords2[i][1] > max_y:
        max_y = coords2[i][1]

rowlist = []
worldlist = []
for i in range(0, max_x+1):
    rowlist.append(0)
for i in range(0, max_y+1):
    worldlist.append(rowlist)

printMap(worldlist)
print(coords1)
print('------')
print(coords2)

# Now draw lines in world
for i in range(0, len(worldlist)):
    if coords1[i][1] == coords2[i][1]:
        ycoord = coords1[i][1]
        print(f'Found line at {coords1[i][1]} and {coords2[i][1]}')
        print(f'length st: {coords1[i][0]} end {coords2[i][0]}')
        print(f'ycoord = {ycoord}')
        # Common X coordinate
        for x in range(coords1[i][0], coords2[i][0]):
            print(f'Writing worldlist[{x}][{ycoord}]')
            worldlist[x][ycoord] = 1
            printMap(worldlist)
            print('xxxxxx')

