'''
Key with the Highest Value
Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.
'''

def max_value_key(my_dict):
    max_value = float('-inf')
    max_key = ''

    for key in my_dict:
        if my_dict[key] > max_value:
            max_key = key
            max_value = my_dict[max_key]
    return max_key

def max_value_key_improved(my_dict):
    return max(my_dict, key=my_dict.get)