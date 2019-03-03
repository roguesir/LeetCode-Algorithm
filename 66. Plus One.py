class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = "".join(map(str, digits))
        if digits.isdigit():
            return map(int, list(str(int(digits) + 1)))
