"""pytest for merge sort."""

from merge import merge_sort
import pytest


def test_sort():
    """test merge sort function on list of ints."""
    a = [123, 55, 2, 7, 22, -10, 1]
    assert merge_sort(a) == [-10, 1, 2, 7, 22, 55, 123]


def test_sort_empty_input():
    """test merge sort function on empty list."""
    a = []
    merge_sort(a)
    assert a == []


def test_sort_letters_input():
    """test merge sort function on list of strings."""
    a = ["a", "b"]
    merge_sort(a)
    assert a == ["a", "b"]
