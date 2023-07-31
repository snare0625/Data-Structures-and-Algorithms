'''
Question: Missing Number
Description: Write a function to find the missing number in a given integer array of 1 to 100.
'''

# Solution 1
def missingNumber(arr, n):
    for i in range(n):
        if i + 1 in arr:
            continue
        else:
            return i + 1
    return 0

