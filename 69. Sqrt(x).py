class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        if x >= 0:
            return int(math.sqrt(x))
