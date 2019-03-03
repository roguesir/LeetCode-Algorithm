class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.isdigit():
            return True
        elif "e" in s and "." in s and s.split("e") == 2:
            s1, s2 = s.split("e")
            try:
                return float(s1) and float(s2)
            except ValueError:
                return False
        else:
            try:
                float(s)
                return True
            except ValueError:
                return False
