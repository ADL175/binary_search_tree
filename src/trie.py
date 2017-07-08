"""Create a trie data structure."""


class Node(object):
    """Implement a node for Trie."""

    def __init__(self, val=None, parent=None):
        """Instantiate a new Trie."""
        self.val = val
        self.parent = parent
        self.children = {}
        self.has_children = False
        self.is_end = False

    def add(self, child):
        """adding a child to parent node."""
        if child in self.children.keys():
            return
        self.children[child] = Node(child, parent=self)


class Trie(object):
    """Implement a binary search Trie."""

    def __init__(self, val=None):
        self._root = Node()
        self._size = 0
        if type(val) in [list, tuple, str]:
            if type(val) is str:
                self.insert(val)
            else:
                for item in val:
                    self.insert(item)
        elif val:
            raise ValueError('Trie only takes list, string, or tuple.')

    def insert(self, val):
        """Insert a value into the Trie."""
        if len(val) == 0:
            return '(first if) That is an empty string!'
        if not self.contains(val):
            current = self._root
            current_index = 0
            while current_index < len(val):
                letter = val[current_index]
                if letter in current.children.keys():
                    current = current.children[letter]
                else:
                    current.add(letter)
                    current.has_children = True
                    current = current.children[letter]
                current_index += 1
            if current_index == len(val):
                current.is_end = True
                self._size += 1
        else:
            return "end of insert, blah blah"

    def contains(self, val):
        """Search for a value, returns T/F."""
        if len(val) == 0:
            return 'That is an empty string!'
        current = self._root
        current_index = 0
        while current_index < len(val):
            if val[current_index] in current.children.keys():
                current = current.children[val[current_index]]
                current_index += 1
            else:
                break
        return current_index == len(val) and current.is_end

    def size(self):
        """Return number of words in the Trie."""
        return self._size

    def remove(self, val):
        """Remove a valuefrom the Trie, or raise exception ."""
        if
