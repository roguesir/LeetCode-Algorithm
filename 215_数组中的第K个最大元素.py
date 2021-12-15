class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 小顶堆
        # import heapq
        # heap = []
        # heapq.heapify(heap)
        # for num in nums:
        #     heapq.heappush(heap, num)
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # return heap[0]

        # 快排+partition
        left, right, target = 0, len(nums) - 1, k - 1
        while True:
            pos = self.partition(nums, left, right)
            if pos == target:
                return nums[pos]
            elif pos > k:  # 要往左找
                right = pos - 1
            elif pos < k:  # 要往右找
                left = pos + 1

    def partition(self, nums, left, right):
        import random
        k = random.randint(left, right)
        pivot = nums[k]
        nums[left], nums[k] = nums[k], nums[left]
        index = left

        for i in range(left + 1, right + 1):
            if nums[i] > pivot:
                index += 1
                nums[i], nums[index] = nums[index], nums[i]
        nums[left], nums[index] = nums[index], nums[left]
        return index

        # def partition(nums, left, right):
        #     import random
        #     k = random.randint(left, right)
        #     print(k)
        #     pivot = nums[k]
        #     nums[left], nums[k] = nums[k], nums[left]
        #     index = left

        #     for i in range(left+1, right+1):
        #         if pivot < nums[i]:
        #             index += 1
        #             nums[i], nums[index] = nums[index], nums[i]
        #     nums[left], nums[index] = nums[index], nums[left]
        #     return index

        # left, right, target = 0, len(nums)-1, k-1
        # while True:
        #     pos = partition(nums, left, right)
        #     # print(nums[:pos])
        #     if pos == target:
        #         print(nums[0:pos+1])
        #         return nums[pos]
        #     elif pos > k:
        #         right = pos - 1
        #     elif pos < k:
        #         left = pos + 1