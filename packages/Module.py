"""
Returning the sorted tuple in the list in ascending order

Args:
     tuples: The list of tuples

Returns:
    array: The sorted tuples in ascending order

Examples:
    >>>sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]

"""
def sort_last(tuples):    
    # your code here
    lst = len(tuples)
    for i in range(0, lst):
        for j in range(0, lst-i-1):
            if (tuples[j][-1] > tuples[j + 1][-1]):
                temp = tuples[j]
                tuples[j]= tuples[j + 1]
                tuples[j + 1]= temp
    return tuples