class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        height = min(heights[left], heights[right]) * (right - left)

        while left < right:
            currHeight = min(heights[left], heights[right]) * (right - left)
            if currHeight > height:
                height = currHeight
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return height