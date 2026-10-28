class Solution:
    def wordLadderLength(self, startWord, targetWord, wordList):
        # target word cannot be formed
        if targetWord not in wordList:
            return 0
        # add words to dictionary for easy retrieval
        wordDict = {}
        for word in wordList:
            wordDict[word] = 1
        from collections import deque
        # initialise queue for bfs
        q = deque()
        q.append(startWord)
        # initialise vis for bfs
        vis = {}
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
                        # if new word is present in wordDict and not present in vis, add it to bfs queue
                        if newWord in wordDict and newWord not in vis:
                            vis[newWord] = 1
                            q.append(newWord)

        return 0








