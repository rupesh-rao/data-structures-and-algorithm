class Solution:
    def wordLadderLength(self, startWord, targetWord, wordList):
        # add words to dictionary for easy retrieval
        wordDict = set(wordList)

        # target word cannot be formed
        if targetWord not in wordDict:
            return 0

        from collections import deque
        # initialise queue for bfs
        q = deque()
        q.append(startWord)

        # initialise depth
        depth = 0
        # perform bfs
        while q:
            depth += 1
            m = len(q)
            for _ in range(m):
                node = q.popleft()
                # return depth if target is reached
                if node == targetWord:
                    return depth
                # add adjacent word to queue by change only one character
                for i in range(len(node)):
                    for j in range(27):
                        # if same character skip
                        if chr(97 + j) == node[i]:
                            continue
                        # create new word excluding character at 'i'
                        newWord = node[:i] + chr(97 + j) + node[i + 1:]
                        # if new word is present in wordDict, add it to bfs queue
                        if newWord in wordDict:
                            wordDict.remove(newWord)
                            q.append(newWord)

        return 0








