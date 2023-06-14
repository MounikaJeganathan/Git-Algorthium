# O(n)


def is_mountain_array(arr):
    if len(arr) < 3:
        return False
    i = 1
    while i < len(arr) and arr[i] > arr[i - 1]:
        i = i + 1
    if i == len(arr):
        return False
    while i < len(arr) and arr[i] < arr[i - 1]:
        i = i + 1

    return i == len(arr)


mountain_array1 = [1, 3, 6, 3]
print(is_mountain_array(mountain_array1))

mountain_array2 = [1, 3, 6, 7]
print(is_mountain_array(mountain_array2))

mountain_array3 = [5, 3, 6, 2]
print(is_mountain_array(mountain_array3))

mountain_array4 = [1, 3]
print(is_mountain_array(mountain_array4))