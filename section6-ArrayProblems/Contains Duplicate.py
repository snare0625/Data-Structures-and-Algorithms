'''
Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example :

Input: nums = [1,2,3,1]
Output: true

'''

def containsDuplicate(nums):
    seen = set()
    for n in nums:
        if n not in nums:
            seen.add(n)
        else:
            return True
    return False