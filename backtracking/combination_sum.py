# https://leetcode.com/problems/combination-sum/

# NOTE: All elements of candidates are distinct. As a result no explicit de-duplication logic is required
class Solution:
    def combinationSum(self, candidates, target):
        # for storing all the combination
        ans = []
        # for storing current combination
        combination = []

        # NOTE: Python Lists are always pass by reference

        def backtrack(index, current_sum):
            if current_sum == 0:
                ans.append(combination[::])  # add a copy of the current combination
                return
            if current_sum < 0 or index >= len(candidates):
                return
            # add number to combination
            combination.append(candidates[index])
            backtrack(index, current_sum - candidates[index])
            # backtrack
            combination.pop()
            backtrack(index + 1, current_sum)

        backtrack(0, target)
        return ans
