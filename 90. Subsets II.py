class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for x in nums:
            result.extend([subset + [x] for subset in result])
        out = []
        for item in result:
            if len(item) == 0:
                out.append(item)
            elif sorted(item) not in out:
                out.append(sorted(item))
        return out
