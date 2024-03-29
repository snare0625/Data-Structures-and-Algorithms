'''
Common Keys
Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.
'''

def merge_dicts(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    for key in merged_dict:
        if key in dict1 and key in dict2:
            merged_dict[key] = dict1[key] + dict2[key]
    return merged_dict

def merge_dicts2(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result