"""pytest for bubble sort, partnered with Elyanil Castro."""

from bubble import bubble_sort
import pytest


def test_bubble():
    """test bubble sort function on list of ints."""
    a = [123,55,2,7,22,-10,1]
    bubble_sort(a)
    assert a == [-10, 1, 2, 7, 22, 55, 123]

def test_bubble_empty_input():
    """test bubble sort function on empty list."""
    a = []
    bubble_sort(a)
    assert a == []

def test_bubble_letters_input():
    """test bubble sort function on list of strings."""
    a = ["a", "b"]
    bubble_sort(a)
    assert a == ["a", "b"]
