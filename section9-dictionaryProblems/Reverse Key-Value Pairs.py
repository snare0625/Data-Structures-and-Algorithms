'''
Reverse Key-Value Pairs
Define a function which takes as a parameter dictionary and returns a dictionary in which everse the key-value pairs are reversed.
'''

def reverse_dict(my_dict):
    new_dict = {value: key for key, value in my_dict.items()}
    return new_dict