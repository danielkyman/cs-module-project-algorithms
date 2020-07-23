'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    zeroes = []
    new_arr = []
    # check to see if there is a zero
    for x in arr:
        if x == 0:
            zeroes.append(0)
            # arr.remove(x)
        else:
            new_arr.append(x)
    if len(zeroes) > 0:
        new_arr.extend(zeroes)
    return new_arr
    # count how many zeros their is

    # delete the zeroes and append them to the end of the list


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
