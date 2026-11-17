class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        max_area = 0
        # (h,w)
        stack = []

        for i in range(len(heights)):
            if i == 0:
                stack.append((heights[i], 1))
                height = heights[i]
                width = 1
            else:
                width = 1

                while stack and stack[-1][0] > heights[i]:
                    popped_h, popped_w = stack.pop()
                    width += popped_w
                    max_area = max(max_area, popped_h * (width - 1))

                if stack and stack[-1][0] == heights[i]:
                    popped_h, popped_w = stack.pop()
                    width += popped_w

                stack.append((heights[i], width))
        
        max_area = max(max_area, stack[-1][0] * stack[-1][1])

        for i in range(len(stack) - 1, 0, -1):
            stack[i-1] = (stack[i-1][0], stack[i-1][1] + stack[i][1])
            max_area = max(max_area, stack[i-1][0] * stack[i-1][1])

        return max_area