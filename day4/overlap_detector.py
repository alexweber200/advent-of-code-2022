# Day 4: find overlap in search parties

overlap = 0
share = 0

with open('./groups', 'r') as lines:
    for line in lines:
        line = line.strip()
        lo1 = int(line.split(',')[0].split('-')[0])
        hi1 = int(line.split(',')[0].split('-')[1])
        lo2 = int(line.split(',')[1].split('-')[0])
        hi2 = int(line.split(',')[1].split('-')[1])
        # check if one group contains the other
        if (lo1 >= lo2 and hi1 <= hi2) or (lo2 >= lo1 and hi2 <= hi1):
            overlap += 1
            print(line, overlap)

        # Part 2: check if the groups overlap at all
        if not (hi1 < lo2 or hi2 < lo1):
            share += 1

print("total number of completely overlapping groups: {}".format(overlap))
print("total number of partially overlapping groups: {}".format(share))


        
