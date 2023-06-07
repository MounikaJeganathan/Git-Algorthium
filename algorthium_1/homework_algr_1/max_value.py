# a = 12
# b = 124
# c = 10
#
# max_value = a
#
# if b > max_value:
#     max_value = b
#
# if c > max_value:
#     max_value = a
# print("The max value is : ", max_value)

#O(1)
def find_max(a, b, c):


    if a > b and a > c:
        return a

    if b > a and b > c:
        return b

    return c

test_result = find_max(10,20,5)
print(test_result)