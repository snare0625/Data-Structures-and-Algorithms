'''
Elementwise Sum
Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.
'''

def tuple_elementwise_sum(tuple1, tuple2):
    output_tuple = ()
    for i in range(len(tuple1)):
        output_tuple = (tuple1[i] + tuple2[i], )
    return output_tuple