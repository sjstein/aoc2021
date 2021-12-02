# D2P1

fname = 'input_p1'
fp = open(fname, 'r')
commands = fp.read().split('\n')
# each element in the commands list now contains a verb and a magnitude delimited with a space
depth = 0
horiz = 0

for command in commands:
    cmd = command.split()
    if cmd[0] == 'up':
        depth -= int(cmd[1])
    elif cmd[0] == 'down':
        depth += int(cmd[1])
    elif cmd[0] == 'forward':
        horiz += int(cmd[1])
    else:
        print(f'Unknown command: {cmd[0]}')

print(f'Ending position @ horiz: {horiz}, depth: {depth}')
print(f'Answer = {horiz * depth}')

