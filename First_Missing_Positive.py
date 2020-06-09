"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""



"""
Intution:

Keep an array of length = length of input and initialize to 0/False
iterate over the array and set corresponding index to True
iterate over the array again and check the first False in the list.

Time complexity: O(n) Space complexity O(n)


Better way to do this would be to
Iterate over the list and eleminate all the bad entries. like num < 0 or
num > len(nums)

hash the indexes.  
input = [3,4,-1,1]
                0,1,2,3,4
after cleanup  [3,4,0,1,0]
hash nums[nums[i]%len(num)] += len(num)                     0,1,2,3,4
==> i=0  nums[3%5] == nums[3] == nums[3] + 5 == 6   nums = [3,4,0,6,0]
==> i=1  nums[4%5] == nums[4] == 0+5 = 5            nums = [3,4,0,6,5]
==> i=2  nums[0%5] == nums[0] == 3+5 = 8            nums = [8,4,0,6,5]
==> i=3  nums[6%5] == nums[1] +5 == 9               nums = [8,9,0,6,5]
==> i=4  nums[5%5] == nums[0] + 5                   nums = [13,9,0,6,5]

Look for 0 in the array and return index
Time complexity: O(n) Space complexity O(1)
"""



class Solution:
    def firstMissingPositive(self, nums):
        nums.append(0)
        length = len(nums)
        for i,num in enumerate(nums):
            if num<0 or num>=length:
                nums[i] = 0
        
        for i, num in enumerate(nums):
            nums[num%length] += length
        
        for i in range(1,length):
            if nums[i]//length == 0:
                return i
        return -1