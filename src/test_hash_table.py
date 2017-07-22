"""Test our implementation of hash table using a large dictionary of words
Hash table data structure, partnered with James Feore and Kurt Maurer.

"""
import pytest
import random


with open('/usr/share/dict/words') as dictionary:
    words = dictionary.read()
list_words = words.split('\n')


random_words = random.sample(list_words, 500)


@pytest.fixture
def complex_hash_table():
    """Hash table for testing."""
    from hash_table import HashTable
    hash_table = HashTable(hash_function='complex')
    for word in random_words:
        hash_table.set(word, word)
    return hash_table


def test_default_size_and_hash():
    """Tests default size and hash."""
    from hash_table import HashTable
    hash_table = HashTable()
    assert (hash_table.hash_function,
            len(hash_table.table)) == (1, 1024)


def test_size_not_float_or_int():
    """Test if the size provided is not a float or int."""
    from hash_table import HashTable
    with pytest.raises(TypeError):
        hash_table = HashTable('word')


def test_size_less_than_512():
    """Tests if the size provided is under 512."""
    from hash_table import HashTable
    with pytest.raises(ValueError):
        hash_table = HashTable(511)


def test_manual_assignment_of_hash():
    """Test a manual assignment of naive or complex hash."""
    from hash_table import HashTable
    complex_hash = HashTable(hash_function='complex')
    naive_hash = HashTable(hash_function='naive')
    assert (complex_hash.hash_function, naive_hash.hash_function) ==(1, 2)


def test_improper_hash_specified():
    """Test if wrong hash_function is entered to raise error."""
    from hash_table import HashTable
    with pytest.raises(ValueError):
        hash_table = HashTable(hash_function='ploppolpasdf')


def test_naive_hash_is_dumb():
    """Tests if naive hash functions as simple hash."""
    from hash_table import HashTable
    hash_table = HashTable(hash_function='naive')
    hash_table._hash('Apollo') == hash_table._hash('Bunker')


def test_naive_hash_causes_many_collisions():
    """Tests if naive hash causes multiple collisions."""
    from hash_table import HashTable
    hash_table = HashTable(hash_function='naive')
    equal = True
    while equal:
        sample_words = random.sample(list_words, 50)
        for word in sample_words:
            hash_table.set(word,word)
        hash_table_words = [hash_table.get(word) for word in sample_words]
        equal = hash_table_words == sample_words
    assert not equal


@pytest.mark.parametrize('word', random_words)
def test__that_we_get_correct_words(word, complex_hash_table):
    """Tests get method on a complex hashed key."""
    assert complex_hash_table.get(word) == word


def test_if_we_get_none_if_key_not_found(complex_hash_table):
    """Tests the parametrize works as expected."""
    assert complex_hash_table.get("potototototo") is None
