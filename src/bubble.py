"""Implement a bubble sort."""

import sys


def bubble_sort(array_of_stuff):
    """Bubble sort function"""
    if not all(isinstance(n, int) for n in array_of_stuff):
        return
    if len(array_of_stuff) == 0:
        return
    for i in range(len(array_of_stuff)):
        did_swap = False
        for j in range(i+1, len(array_of_stuff)):
            if array_of_stuff[j] < array_of_stuff[i]:
                array_of_stuff[j], array_of_stuff[i] = array_of_stuff[i], array_of_stuff[j]
                did_swap = True
            if not did_swap:
                break


if __name__ == '__main__':
    if len(sys.argv) > 1:
        result = bubble_sort(list(sys.argv[1]))
        print("Bubble Sorted list: ", result)
    else:
        import timeit
        from random import randint

        print("Bubble Sort is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order - Wikipedia")

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
            print(timeit.timeit("bubble_sort(test_lists[i])", number=1000, setup="from __main__ import bubble_sort", globals=globals()))
