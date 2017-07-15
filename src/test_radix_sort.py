"""pytest for radix sort."""

from radix_sort import radix_sort
import pytest


def test_bubble():
    """test radix sort function on list of ints."""
    a = [123, 55, 2, 7, 22, -10, 1]
    radix_sort(a)
    assert a == [-10, 1, 2, 7, 22, 55, 123]


def test_bubble_empty_input():
    """test radix sort function on empty list."""
    a = []
    radix_sort(a)
    assert a == []


def test_bubble_letters_input():
    """test radix sort function on list of strings."""
    a = ["a", "b"]
    radix_sort(a)
    assert a == ["a", "b"]
