'''
Introduce:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = {}
        for i in range(len(nums)):
            reduce_ = target - nums[i]
            if res.get(reduce_) is not None:
                return [i, res[reduce_]]
            res[nums[i]] = i