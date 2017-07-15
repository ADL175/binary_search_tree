"""pytest for insertion sort."""

from insertion import insertion_sort
import pytest


def test_bubble():
    """test insertion sort function on list of ints."""
    a = [123, 55, 2, 7, 22, -10, 1]
    insertion_sort(a)
    assert a == [-10, 1, 2, 7, 22, 55, 123]


def test_bubble_empty_input():
    """test insertion sort function on empty list."""
    a = []
    insertion_sort(a)
    assert a == []


def test_bubble_letters_input():
    """test insertion sort function on list of strings."""
    a = ["a", "b"]
    insertion_sort(a)
    assert a == ["a", "b"]
