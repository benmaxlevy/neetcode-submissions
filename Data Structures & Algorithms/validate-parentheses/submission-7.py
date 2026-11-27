class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        closeToOpen = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for char in s:
            if char in closeToOpen:
                if len(stack) == 0 or stack[-1] != closeToOpen[char]:
                    return False
                elif stack[-1] == closeToOpen[char]:
                    stack.pop()
            else:
                stack.append(char)

        return True if len(stack) == 0 else False