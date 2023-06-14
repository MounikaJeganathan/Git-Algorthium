#O(n)
def missing_element(arr_1, arr_2):
    arr_1.sort()
    arr_2.sort()

    for i in range(len(arr_2)):
        if arr_1[i] != arr_2[i]:
            return arr_1[i]
    return arr_1[-1]


my_list = [1, 3, 5, 14, 16, 17]
my_list_1 = [3, 16, 1, 17, 5]

print(missing_element(my_list,my_list_1))