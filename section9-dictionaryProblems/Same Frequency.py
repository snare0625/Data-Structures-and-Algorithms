'''
Same Frequency
Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.
'''

def check_same_frequency(list1, list2):
    list1_hm = {}
    list2_hm = {}

    for n in list1:
        list1_hm[n] = list1_hm.get(n, 0) + 1 

    for n in list2:
        list2_hm[n] = list2_hm.get(n, 0) + 1

    for n in list1:
        if list1_hm[n] != list2_hm[n]:
            return False
    
    return True