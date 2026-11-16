class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        productLeftOfI = [1 for _ in range(len(nums))]
        productRightOfI = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            if i == 0:
                productLeftOfI[i] = 1
            else:
                productLeftOfI[i] = productLeftOfI[i-1] * nums[i - 1]
            
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                productRightOfI[i] = 1
            else:
                productRightOfI[i] = productRightOfI[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            result.append(productLeftOfI[i] * productRightOfI[i])

        return result