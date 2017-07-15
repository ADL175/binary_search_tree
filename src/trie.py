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
            val = val.lower()
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
            if current_index == len(val) and current is not None:
                current.is_end = True
                self._size += 1
        else:
            return "end of insert, blah blah"

    def contains(self, val):
        """Search for a value, returns T/F."""
        if len(val) == 0:
            return 'That is an empty string!'
        val = val.lower()
        current = self._root
        current_index = 0
        while current_index < len(val):
            if val[current_index] in current.children.keys():
                current = current.children[val[current_index]]
                current_index += 1
            else:
                break
        if current is not None:
            return current_index == len(val) and current.is_end
        else:
            return False

    def size(self):
        """Return number of words in the Trie."""
        return self._size

    def remove(self, val):
        """Remove a value from the Trie, or raise exception ."""
        if self.contains(val):
            if len(val) == 0:
                return 'That is an empty string!'
            terminal_node = self.find_terminal_node(val)
            if terminal_node is not None:
                if not terminal_node.has_children:
                    self.remove_word_ending_with_node(terminal_node)
                else:
                    terminal_node.is_end = False
                self._size -= 1
            return True
        else:
            return "The word: {} is not in Trie, nothing to delete.".format(val)

    def find_terminal_node(self, val):
        """Helper for remove method, locates last node of val."""
        return self.find_end_node(val)

    def remove_word_ending_with_node(self, val):
        """Helper for remove method, removes the word."""
        last_node = val
        letter = last_node.val
        while not last_node.has_children:
            last_node = last_node.parent
            last_node.children[letter] = None
            letter = last_node.val
            if last_node.is_end:
                break

    def find_end_node(self, val):
        """Helper for find_terminal_node."""
        current = self._root
        current_index = 0
        while current_index < len(val):
            current = current.children[val[current_index]]
            current_index += 1
        return current if current.is_end else None

    def traversal_helper(self, root, start=""):
        """helper function for traversal."""
        words = []
        previous = start
        if root is not None and root.val is not None:
            previous += root.val
            if root.is_end:
                words.append(previous)
        for child in root.children.values():
            if child:
                temp = self.traversal_helper(child, previous)
                words.extend(temp)
        return words

    def traversal(self, val=""):
        """traverse the trie and return all words."""
        return self.traversal_helper(self._root, val)

# if __name__ == '__main__':  # pragma: no cover
#     poo = Trie(["word", "wordy", "words", "bird", "birdy", "birds"])
#     print(poo.contains("word"))
#     print(poo.remove("wordy"))
#     print(poo.contains("wordy"))
#     print(poo.contains("word"))
#     poo.insert("wordy")
#     print(poo.traversal(""))
