class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return (nums[0])

        pre_max = nums[0]
        pre_min = nums[0]
        now_max = nums[0]
        for i in nums[1:]:
            max0 = pre_max
            min0 = pre_min  # 每次记录前一次的最大最小值
            pre_max = max(max(max0 * i, i), min0 * i)
            pre_min = min(min(min0 * i, i), max0 * i)
            now_max = max(now_max, pre_max)
        return now_max