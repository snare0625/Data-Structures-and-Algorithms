'''
Pairs
Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.
'''

def pair_sum(my_list, target):
    pairs = []
    for i in range(len(my_list)):
        for j in range(i, len(my_list)):
            if i != j and my_list[i] + my_list[j] == target:
                pair = f"{my_list[i]} + {my_list[j]}"
                if pair not in pairs:
                    pairs.append(pair)
    return pairs

staff = pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
print(staff)


    