class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in need:
                return [need[diff], i]
            if n not in need:
                need[n] = i