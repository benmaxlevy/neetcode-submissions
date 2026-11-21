class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                return nums[left]

            mid = (right + left) // 2
            right_of_mid = mid + 1 if mid + 1 < len(nums) else 0
            left_of_mid = mid - 1 if mid - 1 >= 0 else len(nums) - 1

            if nums[left_of_mid] > nums[mid] and nums[right_of_mid] > nums[mid]:
                return nums[mid]
            elif nums[mid] < nums[left]:
                # search left
                right = mid - 1
            else:
                # search right
                left = mid + 1