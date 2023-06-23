# O(n)
#Find min and max no index and sum inbetween them

# Find a sum of elements between min and max elements.
# Min and max elements are not included.
# All numbers are unique.
def sum_betw_min_max(array):
    if len(array) <= 2:
        return 0
    min_index = max_index = i = 0
    min_item = max_item = array[0]

    while i < len(array):
        if array[i] > max_item:
            max_index = i
            max_item = array[i]

        if array[i] < min_item:
            min_index = i
            min_item = array[i]

        i += 1
    return sum(array[min(min_index, max_index) + 1:max(min_index, max_index)])


test_array1 = [17, 4, 7, 3, 2]
test_result1 = sum_betw_min_max(test_array1)
print(test_result1)

test_list2 = [1, 4, 7, 23, 2]  # min = 1, max = 23, sum = 11
test_result2 = sum_betw_min_max(test_list2)
print(test_result2)