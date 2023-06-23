#O(n)

# Given a list of random numbers.
# Find and return the max element and the index of this element
# Example: [1, 45, 33, 76, 9, 10], print [3, 76]
def max_num_index_list(array):
    max_index = 0
    max_num = array[max_index]

    for i in range(1, len(array)):
        if array[i] > max_num:
            max_index = i
            max_num = array[i]

    print("Max index is :", max_index, " Max number is :", max_num)


test_data = [2, 8, 3, 41, 95]
max_num_index_list(test_data)
