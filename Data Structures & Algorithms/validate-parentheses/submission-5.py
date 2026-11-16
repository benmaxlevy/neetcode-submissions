class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ')': '(', '}': '{', ']': '['
        }
        
        for char in s:
            if char in closeToOpen:
                opening = closeToOpen[char]
                if len(stack) > 0 and stack[-1] == opening:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0
            