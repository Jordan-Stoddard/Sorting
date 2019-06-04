Linear Time: O(n)

def foo(n):
    for i in range(n):
        print(i)

foo(1)      # 1 second
foo(10)     # 10 seconds
foo(100)    # 100 seconds


1) Analyze each line in isolation
2) Add any lines that occur in sequence.
3) Multiply any lines that occur in a loop
4) Return profit (answer?)


def foo(n):

sq_root = int(math.sqrt(n))             # O(1)
    for i in range(0, sq_root):         # O(sqrt n)
    print(i)                            # O(1)

4) Answer: O(1) + O(sqrt n)  # choose dominant term because we only care about the terms that grow to be really, really large.

O(sqrt n)

def frotz(n):
    s = 0 #O(1)

    for i in range(n): #O(n):
        for j in range(2 * n):  #O(2 * n)
        s += i * j #O(1)

    return s # O(1)

1 + (n * (2 * n) * 1)) #Simplified below
1 + 2 * n^2  # dominant term == 2 * n^2
2 * n^2 # # drop constant

Profit: O(n^2)

def search(list, value):
    for i in list:
        if i == value:
            return True
    return False

This is O(n) ^^^

---
O(log n)

If you have an algorithm that gets rid of half the data every time, it's probably a O(log n)

bad_binary_search(list, value):
    sort(list)              # O(n log n)
    bsearch(list, value)    # O(log n)

O(n log n) + O(log n) ==
O(n log n)


If I sort first, then I can make binary_searches and making a ton of binary_searches will be pretty fast.

Initially, a linear search is faster than a sort + binary_search, but the linear searches becomes much more expensive over many searches.

-----
Insertion Sort:

We're going to sort books, so let's initialize a Book class.

class Book:
    def __init__(self, t, a, g)
        title = t
        author = a
        genre = g

def insertion_sort(books):
    # loop through the length of books
    for i in range(1, len(books)):
        # save the current index as temp_book
        temp_book = books[i]
        # make a copy of i saved as j
        j = i
            # for each item in books, run a while loop that checks if j is greater than 0
            # and checks if temp_book.genre (the current book's genre),
            # is less than the book at j directly to the left
        while j > 0 and temp_book.genre < books[j - 1].genre:
        # If it is:
        # scoot books over to make room for the one we're sorting.
        books[j] = books[j - 1] 
        # Then decrement the location of j down one to the left
            j -= 1
        # Then set books at j to equal temp_book
        books[j] = temp_book

    return books

