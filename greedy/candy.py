class Solution:
    # Time: O(N), Space: O(N)
    def _better(self, ratings):
        n = len(ratings)
        if n == 0:
            return n
        left = [0] * n
        # minimum number of candy
        left[0] = 1
        # move from left to right
        for i in range(1, n):
            # increase number of candy by 1 if rating is greater
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            # else assign the minimum candy possible
            else:
                left[i] = 1
        # to store cumulative count of candy from right
        right = 1
        ans = max(1, left[n - 1])
        for i in range(n - 2, -1, -1):
            # increase number of candy by 1 if rating is greater
            if ratings[i] > ratings[i + 1]:
                right = right + 1
            else:
                right = 1
            ans += max(left[i], right)

        return ans

    # Time: O(N), Space: O(1)
    def _optimal(self, ratings):
        # minimum candy for the first kid
        ans = 1
        # start with 2nd kid
        i = 1
        n = len(ratings)
        while i < n:
            # add 1 to answer when slope is flat
            if ratings[i] == ratings[i - 1]:
                ans += 1
                i += 1
                continue
            # initialise peak
            peak = 1
            # when slope is positive
            while i < n and ratings[i] > ratings[i - 1]:
                # increase peak first (since we are already adding minimum candy to first kid)
                peak += 1
                # add candy to answer
                ans += peak
                i += 1
            # initialise down peak
            down = 1
            while i < n and ratings[i] < ratings[i - 1]:
                # add to answer first (as the comparison from peak will be done later, we are start from next of peak)
                ans += down
                down += 1
                i += 1
            # add the excess required in the peak
            if down > peak:
                ans += down - peak
        return ans

    def candy(self, ratings):
        if len(ratings) == 0:
            return 0
        # return self._better(ratings)
        return self._optimal(ratings)
