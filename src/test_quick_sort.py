"""pytest for quick sort."""

from quick_sort import quick_sort
import pytest


def test_sort():
    """test quick sort function on list of ints."""
    a = [123, 55, 2, 7, 22, -10, 1]
    quick_sort(a, 0, len(a)-1)
    assert a == [-10, 1, 2, 7, 22, 55, 123]


def test_sort_empty_input():
    """test quick sort function on empty list."""
    a = []
    quick_sort(a, 0, len(a)-1)
    assert a == []


def test_sort_letters_input():
    """test quick sort function on list of strings."""
    a = ["a", "b"]
    quick_sort(a, 0, len(a)-1)
    assert a == ["a", "b"]
