"""
A Trie data structure is a tree-like data structure where each node represents a character of a string sequence. The root node represents an empty string, and each edge represents a character. The path from the root to a node represents a prefix of a string stored in the Trie. This structure allows for efficient insertion, deletion, and search operations.

For example, if we consider a Trie for storing strings with only lowercase characters then each node of the trie will consist of 26 children each representing the presence of letters from a-z. Following are some properties of the trie data structure:

Each node will represent a single character of the string.
The root node represents an empty string.
Each path of the tree represents a word.
Each node of the trie will have 26 pointers to represent the letters from a-z.
A boolean flag is used to mark the end of a word in the path of a Trie.

For more: https://www.geeksforgeeks.org/cpp/trie-data-structure-in-cpp/
"""

# https://leetcode.com/problems/implement-trie-prefix-tree/description/
class TrieNode:
    def __init__(self):
        self.characters = [False] * 26
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            ind = ord(ch) - ord('a')
            if not curr.characters[ind]:
                curr.characters[ind] = TrieNode()
            curr = curr.characters[ind]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            ind = ord(ch) - ord('a')
            if not curr.characters[ind]:
                return False
            curr = curr.characters[ind]
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            ind = ord(ch) - ord('a')
            if not curr.characters[ind]:
                return False
            curr = curr.characters[ind]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)