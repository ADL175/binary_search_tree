#Bubble Sort

w/ Elyanil Castro
bubble.py contains bubble sort function.

Time Complexity Big O(N^2)

#HashTable

Hash table data structure, partnered with James Feore and Kurt Maurer

Hash table utilizes a list of buckets, which buckets are binary search trees. This data structure's methods include a naive hashing / Additive Hash, complex hash, get(key), set(key, val), and hash(key). The HashTable uses a modified binary search tree (store_bst.py).

The Big O time complexity is O(1).


# trie


Trie and Tests created by David Lim and Elyanil Castro

Tries uses: -insert(self, string): will insert the input string into the trie. If character in the input string is already present, it will be ignored.


-contains(self, string): will return True if the string is in the trie, False if not.

-size(self): will return the total number of words contained within the trie. 0 if empty.

-remove(self, string): will remove the given string from the trie. If the word doesn’t exist, will raise an appropriate exception.

-traversal returns list of all words

-autocomplete takes argument and returns autocomplete words.

Big O(N) time complexity N = len(word inserted into the Trie) space complexity = Big O(N)



# binary_search_tree

Binary Search Tree Functions and Tests sourced from Kurt Maurer and James Feore

Partnered w/ James Feore, Kurt Maurer, and Elyanil Castro

Binary Search Tree Implement a binary search tree with insert(), search() size(), depth(), contains(), balance()

BST Traversals Implement the following traversals:

in_order(self) pre_order(self) post_order(self) breadth_first(self)

Each returns a generator that will yield nodes according to their conventions:

https://en.wikipedia.org/wiki/Tree_traversal
