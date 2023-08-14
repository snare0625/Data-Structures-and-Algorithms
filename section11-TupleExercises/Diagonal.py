'''
Diagonal
Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.
'''

def get_diagonal(tup):
    output_tuple = ()
    for i in range(len(tup)):
        output_tuple = output_tuple + (tup[i[i]])
    return output_tuple