elves = [0]
elf = 0

with open('./input', 'r') as lines:
    for line in lines:
        if len(line) > 2:
            elves[elf] += int(line)
        else:
            elf += 1
            elves.append(0)

print('Elf #{} is carrying the most calories, with a total of {}'.format(elves.index(max(elves))+1, max(elves)))