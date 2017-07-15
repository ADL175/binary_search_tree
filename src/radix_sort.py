"""Implement an radix sort."""

import sys


def radix_sort(array_of_stuff):
    """Radix sort function"""
    if not all(isinstance(n, int) for n in array_of_stuff):
        return
    if len(array_of_stuff) == 0:
        return
    if len(array_of_stuff) < 2:
        return array_of_stuff
    positive_nums = list(filter(lambda x: x >= 0, array_of_stuff))
    array_of_stuff = list(filter(lambda x: x < 0, array_of_stuff))
    print(positive_nums, array_of_stuff)
    def sort_func(nums):
        """helper for radix."""
        is_sorted = False
        temp = 0
        divisor = 1
        buckets = [[]]*10
        while not is_sorted:
            is_sorted = True
            for num in nums:
                temp = abs(int(num/divisor))
                buckets[temp % 10].append(num)
                import pdb; pdb.set_trace()
                if is_sorted and temp > 0:
                    is_sorted = False
            idx = 0
            for i in range(0, 9):
                for num in buckets[i]:
                    nums[idx] = num
                    idx += 1
                buckets[i] = []
            divisor *= 10

    sort_func(positive_nums)
    sort_func(array_of_stuff)
    array_of_stuff.extend(positive_nums)


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
