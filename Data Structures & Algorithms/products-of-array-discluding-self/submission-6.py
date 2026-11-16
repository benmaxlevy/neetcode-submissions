class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                result[i] = 1
            else:
                result[i] = result[i-1] * nums[i-1]
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                continue
            else:
                right *= nums[i+1]
                result[i] *= right

        return result