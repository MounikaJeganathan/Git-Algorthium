

#O(N)
# Write a program that takes as input a sorted array and updates it so that all duplicates
# have been removed and the remaining elements have been shifted left to fill the emptied indices.
# Fill the remaining indices with zeroes.
# Return the number of valid elements.
# You cannot use sets for this coding challenge.

# code here
# [1, 1, 2, 2, 3, 4, 5, 5]
# [1, 2, 3, 4, 5, 0, 0, 0]
# write_index = 5
# [1, 2, 3, 4, 5, 0, 0, 0]  # number of valid elements is 5

def delete_duplicate(array):
    write_index = 1

    print("array list before deleting duplicates are ", array)
    for i in range (1,len(array)):
        if array[write_index-1]!=array[i]:
            array[write_index]= array[i]
            write_index+=1

    for i in range(write_index,len(array)):
        array[i]=0

    print("array list After deleting duplicates are ", array)
    return write_index

test_list = [1,1,2,3,3,5,6,6,7,7,7]
result = delete_duplicate(test_list)
print(result)