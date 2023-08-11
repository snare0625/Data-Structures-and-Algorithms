'''
Elementwise Sum
Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.
'''

def tuple_elementwise_sum(tuple1, tuple2):
    output_tuple = ()
    for i in range(len(tuple1)):
        output_tuple = (tuple1[i] + tuple2[i], )
    return output_tuple

# Improved Solution 1
def tuple_elementwise_sum2(tuple1, tuple2):
    return tuple(map(sum, zip(tuple1, tuple2)))

# Improved Solution 2
def tuple_elementwise_sum3(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise("Input tuples must have the same length.")
    
    result = tuple(a + b for a, b in zip(t1, t2))
    return result