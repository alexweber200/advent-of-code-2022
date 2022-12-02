# Day 2: Rock paper scissors strategry guide score calculator (both part methods)
score = 0
score_2 = 0

shape_score = [1, 2, 3]
result_score = [0, 3, 6]
score_matrix = [[3, 0, 6], [6, 3, 0], [0, 6, 3]]
shape_matrix = [[2, 0, 1], [0, 1, 2], [1, 2, 0]]



with open('./guide', 'r') as lines:
    for line in lines:
        choices = line.split(' ')

        you = ord(choices[0]) - ord('A')
        me = ord(choices[1].strip()) - ord('X')


        ''' Following guide incorrectly:
            you:        A   B   C
            me:     X   3   0   6   
                    Y   6   3   0
                    Z   0   6   3
        '''
        # calculate the score based on what we thought
        score += (score_matrix[me][you] + shape_score[me])

        ''' Following guide as the elf intended:
            you:        A   B   C
        my choice:  X   C   A   B   
                    Y   A   B   C
                    Z   B   C   A
        '''

        # calculate the score based on the correct strat
        score_2 += result_score[me] + shape_score[shape_matrix[me][you]]

print("total score following the strat guide initially: {} points".format(score))
print("total score following the strat guide correctly: {} points".format(score_2))