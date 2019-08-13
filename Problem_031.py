"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = len(nums)-1
        while i:
            if nums[i] <= nums[i-1]:
                i-=1
            else:
                j = i

                replacement = i
                while j<len(nums):
                    if nums[j] < nums[replacement] and nums[j]>nums[i-1]:
                        replacement = j
                    j+=1
                nums[i-1],nums[replacement] = nums[replacement],nums[i-1]
                break
        nums =  (nums[:i] + sorted(nums[i:]))
        print(nums)
        return nums  
