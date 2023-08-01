'''
Duplicate Number
Write a function to remove the duplicate numbers on given integer array/list.
'''

def remove_duplicates(my_list):
    distinct_list = []
    for num in my_list:
        if num not in distinct_list:
            distinct_list.append(num)
    return distinct_list