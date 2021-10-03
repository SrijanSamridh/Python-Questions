# You have been given a random integer array/list(ARR) of size N. You have been required to push all the zeros that
# are present in the array/list to the end of it. Also, make sure to maintain the relative order of the non-zero
# elements.
#
# Note: Change in the input array/list itself. You don't need to return or print the elements.
#
# You need to do this in one scan of array only. Don't use extra space.
#
#
# Input format : The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
# Then the test cases follow.
#
# First line of each test case or query contains an integer 'N' representing the size of the array/list.
#
# Second line contains 'N' single space separated integers representing the elements in the array/list.
# Output Format :
# For each test case, print the elements of the array/list in the desired order separated by a single space.
#
# Output for every test case will be printed in a separate line.


def pushZerosAtEnd(arr, n):
    count = 0  # Count of non-zero elements

    # Traverse the array. If element
    # encountered is non-zero, then
    # replace the element at index
    # 'count' with this element
    for i in range(n):
        if arr[i] != 0:
            # here count is incremented
            arr[count] = arr[i]
            count += 1

    # Now all non-zero elements have been
    # shifted to front and 'count' is set
    # as index of first 0. Make all
    # elements 0 from count to end.
    while count < n:
        arr[count] = 0
        count += 1
    # return arr

                                        # WITH ONLY FOR LOOP
def pushZerosAtEnd(arr, n):
    count = 0  # Count of non-zero elements

    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    for j in range(count, n):
        arr[j] = 0
    return arr
