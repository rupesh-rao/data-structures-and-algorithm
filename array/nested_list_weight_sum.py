"""
Given a nested list of integers, compute the sum where each integer is weighted 
by the reverse of its depth (elements deeper in the nesting get smaller weights,
weight = maxDepth − depth + 1). The challenge is handling arbitrary nesting and 
determining appropriate weights across levels to produce the weighted total.

Input:

nestedList = [1,[4,[6]]]
Output:

17

Explanation: Maximum depth is 3. Weighted sum: 13 + 42 + 6*1 = 3 + 8 + 6 = 17

Constraints:

1 <= nestedList.length <= 50
The values of the integers in the nested list are in the range [-100, 100]
The maximum depth of any integer is less than or equal to 50
Each element is either an integer or a list whose elements are also integers or other lists

"""


class Solution:
    def depthSumInverse(self, nums)->int:
        # find the max depth with one DFS
        def findMaxDepth(nested, depth):
            maxDepth = depth
            for item in nested:
                if isinstance(item, list):
                    maxDepth=max(maxDepth, findMaxDepth(item, depth+1))
            return maxDepth

        maxD = findMaxDepth(nums, 1)

        # calculate weighted sum with maxDepth known
        def calculateWeightedSum(nested, dep, maxD):
            total = 0
            for item in nested:
                if isinstance(item, list):
                    total += calculateWeightedSum(item, 1+dep,maxD)
                else:
                    w = maxD-dep+1
                    total += w*item
            return total

        return calculateWeightedSum(nums, 1, maxD)

    def depthSumInverseOnePass(self, nums)->int:
        """
        Uses BFS with clever accumulation: add level sum to total at each level,
        and carry forward previous sums so shallower elements get added more times.
        """
        from collections import deque
        q = deque(nums)
        total_sum = level_sum = 0

        while q:
            size = len(q)
            for _ in range(size):
                item=q.popleft()
                if isinstance(item, int):
                    level_sum += item
                else:
                    for x in item:
                        q.append(x)
            total_sum += level_sum

        return total_sum




if __name__ == '__main__':
    s = Solution()
    print(s.depthSumInverse([1,[4,[6]]])) # 17
    print(s.depthSumInverse([1,[4,6,[6+7]]]))

    print(s.depthSumInverseOnePass([1,[4,[6]]])) # 17
    print(s.depthSumInverseOnePass([1,[4,6,[6+7]]]))
