class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dictionary = {}
        for word in wordDict:
            dictionary[word] = 1
        # store index where word was found
        indices = [-1]
        found = [False]*len(s)
        for i, ch in enumerate(s):
            for j in indices:
                if s[j+1:i+1] in dictionary:
                    found[i] = True
                    indices.append(i)
                    break

        return found[-1]
