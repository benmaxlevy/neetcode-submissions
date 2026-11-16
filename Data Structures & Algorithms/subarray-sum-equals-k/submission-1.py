class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarrays = 0
        prefixFreq = defaultdict(int)
        prefixFreq[0] = 1

        currentVal = 0

        for i,n in enumerate(nums):
            currentVal += n
            subarrays += prefixFreq[currentVal-k]
            prefixFreq[currentVal] += 1
        
        return subarrays