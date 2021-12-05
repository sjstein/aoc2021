# D4P2
card = []   # List of bingo cards
blank = []   # List of blank (to be filled in) cards
row = []    # Contents of row in bingo card
card_count = 0

fname = 'input_p1'
fp = open(fname, 'r')
# First entry is the numbers drawn to determine winner
drawn_nums = fp.readline().split(',')
print(drawn_nums)

def checkNumber(c, m, n):
    """
    c is the list containing all bingo cards
    m is the list containing all cards with positions marked as matches
    n is the number being checked for
    """
    for i in range(0, len(c)):
        for j in range(0, len(c[0])):
            for k in range(0, len(c[0][0])):
                if c[i][j][k] == n:
                    m[i][j][k] = 'X'
    return


def checkBingo(c, m, w):
    """
    :param  c: Card list
            m: Matrix containing filled in bingo card grid locations
            w: list of winning cards already discovered (so now, invalid)
    :return: [bingo?, compute, winning board number]
        bingo: True / False
        compute : computed value of winning row / column
    """
    # Check for winning row
    accum = 0
    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            if m[i][j] == ['X', 'X', 'X', 'X', 'X']:
                # Winning row discovered on card[i]
                if i in w:
                    #print(f'Found duplicate winner, so moving on')
                    break
                # Calculate the return value based on elements not already selected
                for x in range(0, len(m[0])):
                    for y in range(0, len(m[0][0])):
                        if m[i][x][y] == '_':
                            accum += int(c[i][x][y])
                return [True, accum, i]
    # No winning row found, now look for columns
    for i in range(0, len(m)):
        for k in range(0, len(m[0][0])):
            if m[i][0][k] == 'X' and \
                    m[i][1][k] == 'X' and \
                    m[i][2][k] == 'X' and \
                    m[i][3][k] == 'X' and \
                    m[i][4][k] == 'X':
                if i in w:
                    #print('Found duplicate (col) winner, moving on')
                    break
                #print(f'Found a column winner with board {i}')
                for x in range(0, len(m[0])):
                    for y in range(0, len(m[0][0])):
                        if m[i][x][y] == '_':
                            accum += int(c[i][x][y])
                return [True, accum, i]
    return[False, 0, 0]


def printCards(c):
    for i in range(0, len(c)):
        for j in range(0, len(c[0])):
            print(c[i][j])
        print('---')

    return


# Now parse each bingo card into a list, each element of that lists consists of 5 lists of 5 numbers each
#  corresponding to a square array (5x5) representing a given bingo card

for line in fp:
    if line.rstrip() == '':
        card_count += 1
    else:
        row.append(line.rstrip().split())

print(f'found {card_count} cards')
#print(row)

# We now have a list of rows of ALL cards and need to chunk those into a card list
for c in range(0, card_count):
    ind = c * len(row[0])
    card.append([row[ind], row[ind+1], row[ind+2], row[ind+3], row[ind+4]])
    blank.append([['_', '_', '_', '_', '_'],
                 ['_', '_', '_', '_', '_'],
                 ['_', '_', '_', '_', '_'],
                 ['_', '_', '_', '_', '_'],
                 ['_', '_', '_', '_', '_']])
    print(c)

# Iterate through the input list of drawn numbers

printCards(card)
winning_boards = []
for num in drawn_nums:
    print(f'Checking cards with value {num}')
    checkNumber(card, blank, num)
    # printCards(blank)
    ret = checkBingo(card, blank, winning_boards)
    if ret[0]:
        if ret[2] not in winning_boards:
            winning_boards.append(ret[2])
            print(f'Board number {ret[2]} is a WINNER!')
            print(f'found a winner with {ret[1]}')
            print(f'answer: {ret[1] * int(num)}')
            #printCards(blank)
            print('----')





