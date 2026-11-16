class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxLeft = height[left]
        maxRight = height[right]
        rain = 0

        while left < right:
            if height[left] < height[right]:
                left += 1
                maxLeft = max(maxLeft, height[left])
                rain += max(0, maxLeft - height[left])

            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                rain += max(0, maxRight - height[right])

        return rain


