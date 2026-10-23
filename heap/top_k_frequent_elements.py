# https://takeuforward.org/practice/dsa/top-k-frequent-elements
# Time: O(N) + O(NLogK), Space: O(N) + O(K)
class Solution:
    def topKFrequent(self, nums, k):
        n = len(nums)
        freq = {}
        # find the frequency of each element
        for i in range(n):
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        from heapq import heappush, heappop
        pq = []
        # keep a min-heap of (freq, element)
        for key,value in freq.items():
            heappush(pq, (value, key))
            # remove the min freq element if size is greater than k
            if len(pq) > k:
                heappop(pq)

        return [x[1] for x in pq]