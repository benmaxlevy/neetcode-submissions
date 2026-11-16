class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(nlogn)
        nums = sorted(nums)
        result = []
        
        priorK = -1
        # realization: nums[i] + nums[j] = -nums[k]
        for k in range(len(nums) - 2):
            if priorK >= 0 and nums[priorK] == nums[k]:
                priorK += 1
                continue
            
            left = k + 1
            right = len(nums) - 1

            target = -nums[k]

            while left < right:                
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    soln = [nums[k], nums[left], nums[right]]
                    if nums[left] + nums[right] == target and left != right:
                        result.append(soln)
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    
            priorK += 1
                
        return result

                