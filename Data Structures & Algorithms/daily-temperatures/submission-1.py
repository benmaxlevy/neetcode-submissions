class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            if i == 0:
                stack.append(i)
                continue
            else:
                while len(stack) > 0 and t > temperatures[stack[-1]]:
                    update = stack.pop()
                    result[update] = i - update
                stack.append(i)
        
        return result