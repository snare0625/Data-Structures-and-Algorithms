'''
Best Score
Given a list, write a function to get first, second best scores from the list.

List may contain duplicates.
'''

def first_second(scores):
    n = len(scores)
    scores.sort()
    first_score = scores[n - 1]
    second_score = scores[n - 2]
    return (first_score, second_score)