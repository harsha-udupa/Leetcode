"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


"""
Intution:  
Brute-force way of doing this is to iterate over the array twice and check if arr[i]+arr[j] == target:
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if arr[i]+arr[j] == target

Time complexity = O(n^2)       Space complexity = O(1)

Better approach would be store target - arr[i] in a dictionary and as we go on, check arr[i] in the dict.

Time complexity = O(n)       Space complexity = O(n)
"""

class Solution:
    def twoSum(self, nums, target: int):
        diff_recorder = dict()

        for index,num in enumerate(nums):
            if num in diff_recorder:
                return [diff_recorder[num], index]
            diff_recorder[target-num] = index

        return None



def main():
    test_input = {
                    "test_01": ([1,4,2,6,2,3,-5,-3,2,9], -1, [[1,6],[6,1],[2,7],[7,2]]),
                    "test_02": ([1,4,2,6,2,3,-5,-3,2,9], 3, [[0,2],[2,0],[0,4],[4,0], [3,5],[5,3]]),
                    "test_03": ([1,4,2,6,2,3,-5,-3,2,9], 15, [[3,9],[9,3]])
    }

    tester = Solution()
    for key,val in test_input.items():
        print("Running {} .....".format(key))
        assert tester.twoSum(val[0], val[1]) in val[2], "Test case failed:\nTestCase:{test}\n,InputArray:{nums}\n,Target:{target}\n".format(key, val[0], val[1])
        print("passed.")
    print("All tests passed")

if __name__ == "__main__":
    main()