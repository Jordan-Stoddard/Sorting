# TO-DO: Complete the selection_sort() function below 
"""
selection_sort takes in an array.
1) We loop through the array and set the current_minimum value to be the first item in the array's value.
2) Next we start a second loop through the array, but this time starting 1 index to the right of the first loops current index.
3) Inside the second loop, we set our current_compare_item to be the value of the second loop's current index.
4) We then check that to see if the current_compare_item is less than the current_minimum value.
5) If it is, we set a variable called new_minimum_index, to be the second loop's current index, and we set the current_minimum to be the current_compare_item.
6) Once we get through the second loop, if the value of arr[i] is less than the arr[new_minimum_index], then we swap arr[i] and arr[new_minimum_index].
7) Once we've swapped we move begin the second loop again at the 1th index.
8) If we get an UnboundLocalError, it means that we never set a new_minimum_index, because the entire array was already sorted correctly. In this case, we just return the array.
9) Once we've sorted all the items, return the new mutated array.

"""

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_minimum = arr[i]
        for j in range(i + 1, len(arr)):
            cur_compare_item = arr[j]
            if cur_compare_item < cur_minimum:
                new_minimum_index = j
                cur_minimum = cur_compare_item
        try:        
            if arr[i] > arr[new_minimum_index]:
                arr[i], arr[new_minimum_index] = arr[new_minimum_index], arr[i]
        except UnboundLocalError:
            return arr
    return arr

print(selection_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))


"""
bubble_sort takes in an array.
1) We initialize a boolean flag called swapped to be True
2) While swapped is True keep looping:
    *) First set swapped to false inside the while loop
    *) Then run a for loop, starting at 0 and going through the end of the array.
        >) Inside the for loop check to see if the left index is larger than the right index
            if it is swap, then set swapped to True
        >) Continue through for loop until end.
    *) Check if swapped == False, because if we didn't go into the if statement inside of the for loop
then that means no items swapped, which means the entire array is sorted from lowest to highest,
which means that swapped will == False, and the while loop will break
3) return the sorted version of the array.
"""


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(arr) - 1):
            left_side = arr[i]
            right_side = arr[i+1]
            if left_side > right_side:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if swapped == False:
            break
    return arr


# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr