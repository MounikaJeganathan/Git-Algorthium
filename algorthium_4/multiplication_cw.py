# O(n)
# Given an array of integers. Calculate sum and multiplication of elements.
# Return the list, calculated sum, and multiplication of elements
# Example: [1, 7, 3] Return: [11, 21]
def sum_and_multiply(array):
    sum_result= 0
    muliply_result = 1

    for number in array:
        sum_result = number+sum_result
        muliply_result = muliply_result *number

    print(f"Input list is {array} ")
    print("Sum of numbers :",sum_result)
    print("Multiplication  of numbers :",muliply_result)


test_array = [2,3,5]
sum_and_multiply(test_array)
