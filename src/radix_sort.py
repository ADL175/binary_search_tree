"""Implement an radix sort."""

import sys
import math


def radix_sort(iter):
    """Sort the interable using the radix sort method."""
    if not isinstance(iter,(list, tuple)):
        raise TypeError("Input only a list/tuple of integers")
    if not all(isinstance(x, (int, float)) for x in iter):
        raise ValueError("Input only a list/tuple of integers")

    places = 0
    for num in iter:
        digits = num_digits(num)
        if digits > places:
            places = digits

    for place in range(1, places + 1):
        bucket = [[], [], [], [], [], [], [], [], [], []]
        for num in iter:
            digit = get_digit(num, place + 1)
            bucket[digit].append(num)
        iter = []
        for sub in bucket:
            for number in sub:
                iter.append(number)
    return iter


def get_digit(num, place):
    """Return the place-th digit of num."""
    return int(num / 10 ** (place - 1)) % 10


def num_digits(num):
    """Give the length of a given number."""
    if num > 0:
        return int(math.log10(num)) + 1
    elif num == 0:
        return 1


if __name__ == '__main__':
    if len(sys.argv) > 1:
        result = radix_sort(list(sys.argv[1]))
        print("Radix Sorted list: ", result)
    else:
        import timeit
        from random import randint

        print("radix sort is a non-comparative integer sorting algorithm that sorts data with integer keys by grouping keys by the individual digits which share the same significant position and value. - Wikipedia")

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
            print(timeit.timeit("radix_sort(test_lists[i])", number=1000, setup="from __main__ import radix_sort", globals=globals()))
