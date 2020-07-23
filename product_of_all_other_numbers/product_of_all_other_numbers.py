'''
Input: a List of integers
Returns: a List of integers
'''
# import numpy
import math


def product_of_all_other_numbers(arr):
    # Your code here
    new_arr = []
    val = 1
    # iterate over input list most likely by index
    for i in range(len(arr)):
        temp_arr = arr.copy()
        temp_arr.remove(temp_arr[i])
        val = math.prod(temp_arr)
        new_arr.append(val)
        temp_arr = []
        val = 1
    return new_arr
    # multiply all number without the index of the current number

    # append each product in to new arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
