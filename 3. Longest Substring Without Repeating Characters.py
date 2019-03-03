class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_value = 0
        if len(s) <= 1:
            return len(s)
        else:
            for i in range(len(s)):
                res_list = [s[i]]
                for j in range(i+1, len(s)):
                    if s[j] not in res_list:
                        res_list.append(s[j])
                        max_value = max(max_value, len(res_list))
                    else:
                        max_value = max(max_value, len(res_list))
                        break
            return max_value
