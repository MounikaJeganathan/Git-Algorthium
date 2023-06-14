def lowest_element(array):
    array = sorted(array)
    return array[0], array[1]
    # lowest_1 = min(array)
    # array.remove(lowest_1)
    # lowest_2 = min(array)
    # array.remove(lowest_2)
    # return lowest_1,lowest_2


array_1 = [196, 3, 4, 9, 10, 9, 2]
print(lowest_element(array_1))
