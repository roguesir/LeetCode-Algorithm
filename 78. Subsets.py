class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for x in nums:
            result.extend([subset + [x] for subset in result])
        return result
