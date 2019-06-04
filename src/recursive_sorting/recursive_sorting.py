# TO-DO: complete the helper function below to merge 2 sorted leftys
def merge( leftA, rightA ):
    result = []
    while len(leftA) != 0 and len(rightA) != 0: # While left array and right array are not empty
        if leftA[0] < rightA[0]: # If the item at 0 in the left array is larger than the item at 0 in the right array
            result.append(leftA[0]) # append the current leftArr[0] to the result array
            leftA.remove(leftA[0])  # remove the current leftArr[0] from the left array
        else:
            result.append(rightA[0]) # else do the same as above but with the right.
            rightA.remove(rightA[0])
    # In some cases, we'll have an empty array on one side but the other side still has one item left in it
    # Here we check for if either side is empty, if it is, then concat the non-empty side with the result.
    if len(leftA) == 0:
        result += rightA
    else:
        result += leftA
    return result

print(merge([1, 2, 4, 5, 8], [0, 3, 6, 7, 9]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr)//2                    # Split the array in half
        left_half =  merge_sort(arr[:middle])   # Recursively break the left half of the array down individual arrays of 1
        right_half = merge_sort(arr[middle:])   # Recursively break the right half of the array down individual arrays of 1
        return merge(left_half, right_half)     # Return merge(left_half, right_half)

# print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r): 
#     # TO-DO

#     return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr
