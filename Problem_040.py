"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

import copy
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        global_ans = []
        def back_track(nums, sums, array, target):

            if not len(nums):
                return

            for i,j in enumerate(nums):
                if sums + j < target:
                    array.append(j)
                    sums += j
                    if i<len(nums)-1:
                        back_track(nums[i+1:], sums, array, target)
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

        global_ans = sorted(global_ans)
        i=0
        while i<len(global_ans)-1:
            if global_ans[i] == global_ans[i+1]:
                global_ans.pop(i+1)
            else:
                i+=1
        return global_ans
