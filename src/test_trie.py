"""Tests Trie functionality using dictionary of words, with Elyanil Castro."""

import pytest
import random


with open('/usr/share/dict/words') as dictionary:
    words = dictionary.read()

words = words.lower()
list_words = words.split('\n')

RANDOM_WORDS = random.sample(list_words, 500)


def test_insert():
    """Tests insert method, and checks against the count of inserted words and length of inserted list are same."""
    from trie import Trie
    test_Trie = Trie()
    for i in RANDOM_WORDS:
        test_Trie.insert(i)
    assert test_Trie.size() == len(RANDOM_WORDS)


@pytest.mark.parametrize('word', RANDOM_WORDS)
def test_contains(word):
    """tests contains method."""
    from trie import Trie
    test_Trie = Trie(RANDOM_WORDS)
    for i in RANDOM_WORDS:
        assert test_Trie.contains(i) is True


@pytest.mark.parametrize('word', RANDOM_WORDS)
def test_removes(word):
    """tests the remove method."""
    from trie import Trie
    test_Trie = Trie(RANDOM_WORDS)
    assert test_Trie.remove(RANDOM_WORDS[1]) is True
    assert test_Trie.remove(RANDOM_WORDS[50]) is True
    assert test_Trie.remove("wordbird") == 'The word: wordbird is not in Trie, nothing to delete.'


@pytest.mark.parametrize('word', RANDOM_WORDS)
def test_size(word):
    """tests the size method."""
    from trie import Trie
    test_Trie = Trie(RANDOM_WORDS)
    assert test_Trie.size() == 500


def test_traversal():
    """Test traversal method."""
    from trie import Trie
    test_Trie = Trie(["word", "wordy", "bird", "words"])
    assert test_Trie.traversal() == ['word', 'wordy', 'words', 'bird']


def test_autocomplete():
    """Test autocomplete method."""
    from trie import Trie
    test_Trie = Trie(["word", "wordy", "bird", "words"])
    assert test_Trie.autocomplete("wo") == ['word', 'wordy', 'words']
    assert test_Trie.autocomplete("b") == ['bird']
