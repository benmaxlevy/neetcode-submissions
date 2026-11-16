class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed_pairs = {}
        for i in range(len(position)):
            position_speed_pairs[position[i]] = speed[i]
        sorted_pairs = sorted(position_speed_pairs.items())
        position = [k for k, _ in sorted_pairs]
        speed = [v for _, v in sorted_pairs]
        
        fleets = 0

        stack = []

        for i in range(len(position)):
            if i == 0:
                stack.append(i)
            else:
                p_1 = position[i]
                s_1 = speed[i]
                
                merged = 0
                while len(stack) > 0 and speed[stack[-1]] > s_1 and (p_1-position[stack[-1]])/(speed[stack[-1]] - s_1) <= (target - p_1)/s_1:
                    stack.pop()
                    merged += 1

               
                stack.append(i)

        fleets += len(stack)
        
        return fleets
