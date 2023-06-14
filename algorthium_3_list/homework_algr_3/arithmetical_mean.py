def arithemetic_mean(array):
    length = len(array)
    total_sum = 0
    for i in array:
        total_sum = total_sum + i
    print(total_sum)
    arr_mean = total_sum / length
    print(arr_mean)
    array_result = []
    for num in array:
        if num < arr_mean:
            array_result.append(num)

    return array_result


array_1 = [1, 3, 5, 6, 4, 10, 2, 3]
print(arithemetic_mean(array_1))
