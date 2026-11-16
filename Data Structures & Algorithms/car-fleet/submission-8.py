class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pairs = sorted(zip(position, speed))
        position = [k for k, _ in sorted_pairs]
        speed = [v for _, v in sorted_pairs]
        
        stack = []

        for i in range(len(position)):
            if i == 0:
                stack.append(i)
            else:
                p_1 = position[i]
                s_1 = speed[i]
                
                while len(stack) > 0 and speed[stack[-1]] > s_1 and (p_1-position[stack[-1]])/(speed[stack[-1]] - s_1) <= (target - p_1)/s_1:
                    stack.pop()

                stack.append(i)

        return len(stack)
