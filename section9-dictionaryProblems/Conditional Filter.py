'''
Conditional Filter
Define a function that takes a dictionary as a parameter and returns a dictionary with elements based on a condition.
'''

def filter_dict(my_dict, condition):
    return {k: v for k, v in my_dict.items() if condition(k,v)}