"""Implement an insertion sort.
partnered with w/ Elyanil Castro
"""

import sys


def insertion_sort(array_of_stuff):
    """Insertion sort function"""
    if not all(isinstance(n, int) for n in array_of_stuff):
        return
    if len(array_of_stuff) == 0:
        return
    for i in range(1, len(array_of_stuff)):
        r = i
        temp_idx = array_of_stuff[i]
        while r > 0 and array_of_stuff[r-1] > temp_idx:
            array_of_stuff[r] = array_of_stuff[r-1]
            r -= 1
        array_of_stuff[r] = temp_idx


if __name__ == '__main__':
    if len(sys.argv) > 1:
        result = insertion_sort(list(sys.argv[1]))
        print("Insertion Sorted list: ", result)
    else:
        import timeit
        from random import randint

        print("Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. - Wikipedia")

        test_list1 = [randint(0, 10) for i in range(10)]
        test_list2 = [randint(0, 100) for i in range(10)]
        test_list3 = [randint(0, 100) for i in range(100)]
        test_list4 = [randint(0, 1000) for i in range(100)]
        test_list5 = [randint(0, 100) for i in range(1000)]
        test_list6 = [randint(0, 1000) for i in range(1000)]
        test_lists = [test_list1, test_list2, test_list3,
                      test_list4, test_list5, test_list6]
        test_desc = ["[randint(0, 10) for i in range(10)]",
                     "[randint(0, 100) for i in range(10)]",
                     "[randint(0, 100) for i in range(100)]",
                     "[randint(0, 1000) for i in range(100)]",
                     "[randint(0, 100) for i in range(1000)]",
                     "[randint(0, 1000) for i in range(1000)]"]

        for i in range(len(test_lists)):
            print("Testing: ", test_desc[i])
            print(timeit.timeit("insertion_sort(test_lists[i])", number=1000, setup="from __main__ import insertion_sort", globals=globals()))
