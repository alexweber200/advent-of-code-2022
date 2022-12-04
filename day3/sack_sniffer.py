# Day 3: Sniff the sack contents, sort them by priority, and report the higest priority
bag_num = 0
matches = []

with open('./sacks', 'r') as lines:
    for line in lines:
        matches.append([])
        line = line.strip()
        sack = [line[:int(len(line)/2)] , line[int(len(line)/2):]]
        comp = [[], []]

        for i in range(0,len(sack[0])):
            comp[0].append(ord(sack[0][i]))
            comp[1].append(ord(sack[1][i]))
            # If the item appears in both, add to common item list
            if sack[0][i] in sack[1]:
                matches[bag_num].append(sack[0][i])

        bag_num +=1

#bag_num -= 1
priorities = []
for i in range(0, bag_num):
    priorities.append(0)
    for item in matches[i]:
        if ord(item) >= ord('a'):
            priority = ord(item) - ord('a') + 1
        else:
            priority = ord(item) - ord('A') + 27
        
        if priority > priorities[i]:
            priorities[i] = priority

print("The sum of the highest shared piority items: {}".format(sum(priorities)))