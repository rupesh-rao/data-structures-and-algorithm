class Solution:

    def combinationSum2(self, candidates, target):
        # Step 1: Sort the candidates to group duplicates together
        candidates.sort()

        ans = []
        combination = []

        def backtrack(index, current_sum):
            if current_sum == 0:
                ans.append(combination[::])  # add a copy of the current combination
                return
            if current_sum < 0 or index >= len(candidates):
                return

            # Choice 1: Include the current number
            combination.append(candidates[index])
            # index + 1 because each number can only be used once
            backtrack(index + 1, current_sum - candidates[index])
            combination.pop()

            # Choice 2: Exclude the current number and skip all its duplicates
            next_index = index + 1
            while (
                next_index < len(candidates)
                and candidates[next_index] == candidates[index]
            ):
                next_index += 1
            backtrack(next_index, current_sum)

        backtrack(0, target)
        return ans
