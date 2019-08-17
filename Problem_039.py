"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

import copy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:


        global_ans = []
        def back_track(nums, sums, array, target):

            if not len(nums):
                return

            for i,j in enumerate(nums):
                if sums + j < target:
                    array.append(j)
                    sums += j
                    back_track(nums[i:], sums, array, target)
                    array.pop()
                    sums -= j

                elif sums + j == target:
                    array.append(j)

                    global_ans.append(copy.copy(array))
                    array.pop()
                    return
                else:
                    return

        nums = sorted(candidates)

        if not len(nums):
            return []
        back_track(nums, 0, [], target)
        return global_ans
