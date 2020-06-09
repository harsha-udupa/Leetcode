"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

"""


"""
Intution: 

 nums = [-1, 0, 1, 2, -1, -4]

 sort the nums: [-4, -1, -1, 0, 2]
 1. Iterate over the array 1s, and take 2 pointers at i+1 & len(arr)-1
 2. If sum > 0: decrement last pointer
 3. If sum < 0: increment first pointer
 4. Add to the answer set

Time complexity O(n^2) Space complexity: O(1)
"""

class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        answer = set()
        for iter_i in range(len(nums)-2):
            if iter_i > 0 and nums[iter_i] == nums[iter_i-1]:
                continue
            iter_j = iter_i + 1
            iter_k = len(nums)-1
            while iter_j < iter_k:
                tempSum = nums[iter_i] + nums[iter_j] + nums[iter_k]
                if tempSum == 0:
                    answer.add((nums[iter_i], nums[iter_j], nums[iter_k]))
                    
                if tempSum > 0:
                    iter_k -= 1
                else:
                    iter_j += 1
        return list(answer)