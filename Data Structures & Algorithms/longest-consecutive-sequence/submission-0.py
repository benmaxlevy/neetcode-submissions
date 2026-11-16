class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        starts = set()
        maxLen = 0
        for num in nums:
            if num-1 not in uniqueNums:
                starts.add(num)
                length = 1

                curr = num
                while curr + 1 in uniqueNums:
                    length += 1
                    curr += 1

                if maxLen < length:
                    maxLen = length

        return maxLen