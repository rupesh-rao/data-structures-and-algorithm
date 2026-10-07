# https://takeuforward.org/practice/dsa/trie-implementation-and-operations

class TrieNode:
    def __init__(self):
        self.characters = [False] * 26
        self.isWord = 0
        self.isPrefix = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for i in word:
            ind = ord(i) - ord('a')
            if not curr.characters[ind]:
                curr.characters[ind] = TrieNode()
            curr = curr.characters[ind]
            curr.isPrefix += 1
        curr.isWord += 1

    def countWordsEqualTo(self, word):
        """
        :type word: str
        :rtype: int
        """
        curr = self.root
        for i in word:
            ind = ord(i) - ord('a')
            if not curr.characters[ind]:
                return 0
            curr = curr.characters[ind]
        return curr.isWord

    def countWordsStartingWith(self, prefix):
        """
        :type word: str
        :rtype: int
        """
        curr = self.root
        for i in prefix:
            ind = ord(i) - ord('a')
            if not curr.characters[ind]:
                return 0
            curr = curr.characters[ind]
        return curr.isPrefix

    def erase(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for i in word:
            ind = ord(i) - ord('a')
            curr = curr.characters[ind]
            curr.isPrefix -= 1
        curr.isWord -= 1

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)