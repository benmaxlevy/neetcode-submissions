import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        result = []
        to_delete = defaultdict(int)
        heap = []
        left = 0

        for right in range(len(nums)):
            while left < right and right - left + 1 > k:
                to_delete[nums[left]] += 1
                left += 1

            heapq.heappush_max(heap, nums[right])

            while len(heap) > 0 and heap[0] in to_delete and to_delete[heap[0]] > 0:
                to_delete[heap[0]] -= 1
                heapq.heappop_max(heap)

            if right - left + 1 == k:
                result.append(heap[0])
    
        return result