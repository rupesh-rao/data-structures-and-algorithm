class Solution:
    def findSequences(self, beginWord, endWord, wordList):
        # add words to set for easy retrieval
        wordDict = set(wordList)
        wordDict.discard(beginWord)

        # target word cannot be formed
        if targetWord not in wordDict:
            return []

        from collections import deque
        # initialise queue for bfs
        q = deque()
        q.append([startWord])

        # to erase elements from set
        # after traversal of a level
        toErase = set()

        # perform bfs
        res = []
        while q:
            m = len(q)
            for _ in range(m):
                words = q.popleft()
                # last word of the sequence
                word = words[-1]

                # target reached
                if word == endWord:
                    if not res:  # first sequence
                        res.append(words)
                    elif len(res[-1]) == len(words):  # sequence with shortest length only
                        res.append(words)

                # add adjacent word to queue by change only one character
                for i in range(len(word)):
                    for j in range(27):
                        # if same character skip
                        if chr(97 + j) == word[i]:
                            continue
                        # create new word excluding character at 'i'
                        newWord = word[:i] + chr(97 + j) + word[i + 1:]

                        # if new word is present in wordDict, add it to bfs queue
                        if newWord in wordDict:
                            words.append(newWord)
                            q.append(words[::])
                            words.pop()
                            # add it in set to remove later, after this level is done
                            # this allows two or more word in current level to reach newWord
                            toErase.add(newWord)
            # remove the words used in this level
            for it in toErase:
                wordDict.discard(it)
            # empty the set
            toErase.clear()
            # greedily break as all the sequence with shortest length would have been added already
            if res:
                break
        return res
