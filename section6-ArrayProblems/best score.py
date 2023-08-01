'''
Best Score
Given a list, write a function to get first, second best scores from the list.

List may contain duplicates.
'''

# first solution
def first_second(scores):
    n = len(scores)
    scores.sort()
    first_score = scores[n - 1]
    second_score = scores[n - 2]
    return (first_score, second_score)

# second solution
def first_second_2(scores):
    max1, max2 = float('-inf'), float('-inf')

    for num in scores:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num
    
    return max1, max2