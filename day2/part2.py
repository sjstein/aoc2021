# D2P2

fname = 'input_p1'
fp = open(fname, 'r')
commands = fp.read().split('\n')
# each element in the commands list now contains a verb and a magnitude delimited with a space
depth = 0
horiz = 0
aim = 0

for command in commands:
    cmd = command.split()
    if cmd[0] == 'up':
        aim -= int(cmd[1])
    elif cmd[0] == 'down':
        aim += int(cmd[1])
    elif cmd[0] == 'forward':
        horiz += int(cmd[1])
        depth += aim * int(cmd[1])
    else:
        print(f'Unknown command: {cmd[0]}')

print(f'Ending position @ horiz: {horiz}, depth: {depth}, aim: {aim}')
print(f'Answer = {horiz * depth}')

