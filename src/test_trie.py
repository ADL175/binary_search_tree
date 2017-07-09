"""Tests Trie functionality using dictionary of words."""

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
    """."""
    from trie import Trie
    test_Trie = Trie(RANDOM_WORDS)
    for i in RANDOM_WORDS:
        assert test_Trie.contains(i) is True


@pytest.mark.parametrize('word', RANDOM_WORDS)
def test_removes(word):
    """."""
    from trie import Trie
    test_Trie = Trie(RANDOM_WORDS)
    assert test_Trie.remove(RANDOM_WORDS[1]) is True
    assert test_Trie.remove(RANDOM_WORDS[50]) is True
    assert test_Trie.remove("wordbird") == 'The word: wordbird is not in Trie, nothing to delete.'


@pytest.mark.parametrize('word', RANDOM_WORDS)
def test_size(word):
    """."""
    from trie import Trie
    test_Trie = Trie(RANDOM_WORDS)
    assert test_Trie.size() == 500
