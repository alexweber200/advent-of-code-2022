# Part 1: Find the elf carrying the most calories
elves = [0]
elf = 0

with open('./input', 'r') as lines:
    for line in lines:
        if len(line) > 2:
            elves[elf] += int(line)
        else:
            elf += 1
            elves.append(0)

# Part 2: Find the top three elves and get the total number of calories held by all 3
text = ['', 'second ', 'third ']
total = 0

for elf in range(0,3):
    max_index = elves.index(max(elves))
    total += max(elves)
    print('Elf #{} is carrying the {}most calories, with a total of {}'.format(max_index+1, text[elf], max(elves)))
    elves.pop(max_index)

print('\nThe top 3 elves are carrying a total of {} calories'.format(total))