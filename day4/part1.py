# D4P1

fname = 'input_p1'
fp = open(fname, 'r')
drawn_nums = fp.readline().split(',')
card = []   # List of bingo cards
blank = []   # List of blank (to be filled in) cards
row = []    # Contents of row in bingo card
card_count = 0

print(drawn_nums)

for line in fp:
    if line.rstrip() == '':
        card_count += 1
    else:
        row.append(line.rstrip().split())

print(f'found {card_count} cards')
# We now have a list of rows of ALL cards and need to chunk those into a card list
for c in range(0, card_count):
    card.append([row[c],row[c+1],row[c+2],row[c+3],row[c+4]])
    c += len(row[0])

# Now the list card contains five rows (lists) of numbers
# We will need to input a number and return a