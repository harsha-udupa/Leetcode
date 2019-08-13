"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def bin_search(arr, tar):

            if not len(arr):
                return -1

            l = 0
            r = len(arr)-1

            while l<r:

                mid = int((l+r)/2)

                if arr[mid] == tar:
                    return mid
                if arr[mid] > tar:
                    r = mid-1
                else:
                    l = mid+1

            if arr[l]== tar:
                return l
            return -1

        index = bin_search(nums, target)
        if index == -1:
            return [-1,-1]
        ans =[]
        i = index
        while i>=0:
            if nums[i] != target:

                break
            i-=1
        ans.append(i+1)
        i=index
        while i<len(nums):
            if nums[i] != target:
                break
            i+=1
        ans.append(i-1)
        return ans
