'''
    Middle Function
    Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
'''

def middle(myList):
    return myList[1:-1]
    
myList = [1, 2, 3, 4]
middle(myList)  # [2,3]