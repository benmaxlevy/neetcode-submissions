class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill = sorted(skill)
        target = skill[0] + skill[-1]

        chemistry = 0

        left = 0
        right = len(skill) - 1

        while left < right:
            if skill[left] + skill[right] == target:
                chemistry += skill[left] * skill[right]
                
                left += 1
                right -= 1
            else:
                return -1

        return chemistry
