# https://takeuforward.org/practice/dsa/kmp-algorithm-or-lps-array
class Solution:
    def LPS(self, pat):
        n = len(pat)
        # stores the length of the longest prefix that is a suffix at 'i'
        # 0 1 2 3 4 5 6
        # compare s[0,2] with s[4:6] if at 6
        lps = [0] * n
        # start with index 1, 0 index will always be 0
        # note: we are not comparing suffix that starts from 0

        i = 1 # index of suffix end
        j = 0 # index of prefix start
        while i < n:
            # when ith element match with jth
            if pat[i] == pat[j]:
                # j is the index of prefix end, so j+1 length is stored
                lps[i] = j + 1
                i += 1
                j += 1
            else:
                while j > 0 and pat[i] != pat[j]:
                    # while it doesn't match, move to length of last lps
                    j = lps[j - 1]
                if pat[i] == pat[j]:
                    lps[i] = j + 1
                    i += 1
                    j += 1
                else:
                    i += 1
        return lps

    def search(self, pat, txt):
        ans = []
        lps = self.LPS(pat + '$' + txt)
        for i in range(len(lps)):
            # pat matches in text whenever lps is length of pattern
            if lps[i] == len(pat):
                ans.append(i - 2 * len(pat))
        return ans



