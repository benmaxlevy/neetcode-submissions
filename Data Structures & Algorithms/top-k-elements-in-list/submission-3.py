class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFrequencies = defaultdict(int)
        for num in nums:
            numFrequencies[num] += 1
        buckets = [[] for _ in range(len(nums))]
        for num, frequency in numFrequencies.items():
            buckets[frequency - 1].append(num)
        
        result = []
        for i in range(len(buckets)-1, -1, -1):
            if len(buckets[i]) > 0:
                result.extend(buckets[i])
            if len(result) == k:
                return result
        return result