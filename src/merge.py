"""Implement an merge sort, partnered with Elyanil Castro ."""

import sys


def merge_sort(array_of_stuff):
    """Merge sort function"""
    if not all(isinstance(n, int) for n in array_of_stuff):
        return
    if len(array_of_stuff) == 0:
        return
    if len(array_of_stuff) < 2:
        return array_of_stuff
    left_list = []
    right_list = []
    mid = int(len(array_of_stuff)/2)
    for idx in range(0, mid):
        left_list.append(array_of_stuff[idx])
    for idx in range(mid, len(array_of_stuff)):
        right_list.append(array_of_stuff[idx])
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return merge_helper(left_list, right_list)


def merge_helper(left, right):
    i = 0
    j = 0
    sorted_array = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    while i < len(left):
        sorted_array.append(left[i])
        i += 1
    while j < len(right):
        sorted_array.append(right[j])
        j += 1
    return sorted_array


if __name__ == '__main__':
    if len(sys.argv) > 1:
        result = merge_sort(list(sys.argv[1]))
        print("Merge Sorted list: ", result)
    else:
        import timeit
        from random import randint

        print("Merge is an efficient, general-purpose, comparison-based sorting algorithm. Most implementations produce a stable sort, which means that the implementation preserves the input order of equal elements in the sorted output. - Wikipedia")

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
            print(timeit.timeit("merge_sort(test_lists[i])", number=1000, setup="from __main__ import merge_sort", globals=globals()))
