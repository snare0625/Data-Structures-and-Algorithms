'''
Sum and Product
Write a function that calculates the sum and product of all elements in a tuple of numbers.
'''

def sum_product(input_tuple):
    sum_input_tuple = 0
    prod_input_tuple = 1

    for n in input_tuple:
        sum_input_tuple += n 
        prod_input_tuple *= n

    return sum_input_tuple, prod_input_tuple

