class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        for i in range(n):
            if i==0:
                max_right[0] = height[-1]
                max_left[0] = height[0]
            else:
                max_left[i] = max(height[:i+1])
                max_right[-i] = max(height[-i:])
        print(max_left)
        print(max_right)
        print(height)
        res = 0
        for i, v in enumerate(height):
            res += max(min(max_left[i], max_right[i]) - v, 0)
        return res