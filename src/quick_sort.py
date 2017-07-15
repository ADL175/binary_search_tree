"""Implement an quick sort."""

import sys
from random import randint


def quick_sort(array_of_stuff, start, end):
    """Quick sort function"""
    if not all(isinstance(n, int) for n in array_of_stuff):
        return
    if len(array_of_stuff) == 0:
        return
    if len(array_of_stuff) < 2:
        return array_of_stuff

    if start < end:
        pivot_pt = randomized_partition(array_of_stuff, start, end)
        quick_sort(array_of_stuff, start, pivot_pt - 1)
        quick_sort(array_of_stuff, pivot_pt + 1, end)


def randomized_partition(array_of_stuff, start, end):
    """Randomize the pivot point."""
    pivot_idx = randint(start, end)
    swap(array_of_stuff, pivot_idx, end)
    return partition(array_of_stuff, start, end)


def swap(array_of_stuff, start, end):
    """Swaps the elements in a collection."""
    array_of_stuff[start], array_of_stuff[end] = array_of_stuff[end], array_of_stuff[start]


def partition(array_of_stuff, start, end):
    """items < pivot pt on left, items > pivot pt on right."""
    pivot = array_of_stuff[end]
    p_idx = start
    for i in range(start, end):
        if array_of_stuff[i] <= pivot:
            swap(array_of_stuff, i, p_idx)
            p_idx += 1
    swap(array_of_stuff, p_idx, end)
    return p_idx


if __name__ == '__main__':
    if len(sys.argv) > 1:
        result = quick_sort(list(sys.argv[1]), 0, len(list(sys.argv[1]))-1)
        print("Quick Sorted list: ", result)
    else:
        import timeit

        print("Quick sort is an efficient sorting algorithm, serving as a systematic method for placing the elements of an array in order. - Wikipedia")

        test_list1 = [randint(0, 10) for i in range(10)]
        test_list2 = [randint(0, 100) for i in range(10)]
        test_list3 = [randint(0, 100) for i in range(100)]
        test_list4 = [randint(0, 1000) for i in range(100)]
        test_lists = [test_list1, test_list2, test_list3,
                      test_list4]
        test_desc = ["[randint(0, 10) for i in range(10)]",
                     "[randint(0, 100) for i in range(10)]",
                     "[randint(0, 100) for i in range(100)]",
                     "[randint(0, 1000) for i in range(100)]"]

        for i in range(len(test_lists)):
            print("Testing: ", test_desc[i])
            print(timeit.timeit("quick_sort(test_lists[i], 0, len(test_lists[i])-1 )", number=1000, setup="from __main__ import quick_sort", globals=globals()))
