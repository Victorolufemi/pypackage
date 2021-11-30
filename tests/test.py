from packages import Module

def sort_last():
    """
    make sure sorted algorithms works correctly
    """
    
    assert Module.sorted_last([(4, 2), (1, 0, 9), (2, 7), (1, 1, 0), (2, 4, 8)]) == [(1, 1, 0), (4, 2), (2, 7), (2, 4, 8), (1, 0, 9)], 'incorrect'
    assert Module.sorted_last([(3, 1, 9), (2, 6), (5, 7, 1)]) == [(5, 7, 1), (2, 6), (3, 1, 9)] , 'incorrect'
    assert Module.sorted_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]) == [(2, 2), (1, 3), (3, 4, 5), (1, 7)], 'incorrect'
