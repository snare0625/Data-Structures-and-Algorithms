'''
Max Product of Two Integers
Find the maximum product of two integers in an array where all elements are positive.
'''

def maxProduct(nums):
    return nums[len(nums) - 1] * nums[len(nums) - 2]