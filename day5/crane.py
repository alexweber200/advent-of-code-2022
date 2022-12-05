# Day 5 - Crane stack

STACKS = 9
POS = 4
height = 0
parse_stacks = True

# initialise the stack array
stacks = [[], [], [], [], [], [], [], [], []]

with open('./stacks', 'r') as lines:
    for line in lines:
        if parse_stacks:
            for i in range(0, STACKS):
                char = line[(i*POS) + 1]
                # done reading stack stuff
                if char == '1':
                    parse_stacks = False
                    break
                # There is an item at the stack position
                if char != ' ':
                    stacks[i].insert(0, char)
        elif 'move' in line:
            instr = line.split(' ')
            boxes = int(instr[1])
            src = int(instr[3]) - 1
            dest = int(instr[5].strip()) - 1

            for op in range(0, boxes):
                stacks[dest].append(stacks[src].pop())

# Print final array
print("Final arrangement of top box items with the cratemover 9000:")
for x in range(0,STACKS):
    print(stacks[x][-1], end='')
print()

stacks = [[], [], [], [], [], [], [], [], []]
parse_stacks = True

# Part 2: Wait, it's the cratemover 9001!!
with open('./stacks', 'r') as lines:
    for line in lines:
        if parse_stacks:
            for i in range(0, STACKS):
                char = line[(i*POS) + 1]
                # done reading stack stuff
                if char == '1':
                    parse_stacks = False
                    break
                # There is an item at the stack position
                if char != ' ':
                    stacks[i].insert(0, char)
        elif 'move' in line:
            instr = line.split(' ')
            boxes = int(instr[1])
            src = int(instr[3]) - 1
            dest = int(instr[5].strip()) - 1
            temp = []

            for op in range(0, boxes):
                temp.append(stacks[src].pop())

            for op in range(0, boxes):
                stacks[dest].append(temp.pop())

# Print final array
print("Final arrangement of top box items with the cratemover 9001:")
for x in range(0,STACKS):
    print(stacks[x][-1], end='')
print()