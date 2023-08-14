'''
Common Elements
Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.
'''

def common_elements(tuple1, tuple2):
    output_tuple = ()
    for i in range(len(tuple1)):
        if tuple1[i] in tuple2:
            output_tuple = output_tuple + (tuple1[i], )
    
    return output_tuple

# Cleaner and improved solution
def common_elements_2(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))