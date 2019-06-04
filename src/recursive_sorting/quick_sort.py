int_list = [5, 9, 3, 7, 2, 8, 1, 6]

def partition(l):
    left = []
    pivot = l[0]
    right = []
    
    for v in l[1:]:
        if v <= pivot:
            left.append(v)
        else:
            right.append(v)

    return left, pivot, right

def quick_sort(l):
    if len(l) <= 1:
        return l

    left, pivot, right = partition(l)

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(int_list))

# # In place quick_sort
#     def quick_sort_A( books, low, high ):
#     # base case
#     if low >= high:
#         return books
#     # recursive case
#     else:
#         # divide
#         pivot_index = low
#         # for each element in subarray
#         for i in range(low, high):
#             if books[i].genre < books[pivot_index].genre:
#                 # double swap to move smaller elements to correct index
#                 # move current element to the right of pivot
#                 temp = books[pivot_index+1]
#                 books[pivot_index+1] = books[i]
#                 books[i] = temp

#                 # swap pivot with element on its right
#                 temp = books[pivot_index]
#                 books[pivot_index] = books[pivot_index+1]
#                 books[pivot_index+1] = temp
#                 pivot_index += 1

#         # conquer
#         # Quick Sort everything left of the pivot
#         books = quick_sort_A(books, low, pivot_index)
#         # Quick Sort everything right of the pivot
#         books = quick_sort_A(books, pivot_index+1, high)
  
#         return books