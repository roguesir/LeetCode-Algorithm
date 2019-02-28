'''
Introduce:
Given a 32-bit signed integer, reverse digits of an integer.
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        y = ""
        if x[0] == "-":
            y = y + x[0]
            for i in range(len(x)-1, 0, -1):
                y += x[i]
        else:
            for i in range(len(x)-1, -1, -1):
                y += x[i]
        if int(y) > 2**31-1 or int(y) < -2**31:
            return 0
        else:
            return int(y)
            