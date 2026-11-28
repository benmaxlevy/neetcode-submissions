class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        target = min(skill) + max(skill)

        needToIndex = defaultdict(int)

        chemistry = 0

        for s in skill:
            if s in needToIndex:
                chemistry += s * (target - s)

                if needToIndex[s] == 1:
                    del needToIndex[s]
                else:
                    needToIndex[s] -= 1
            else:
                needToIndex[target - s] += 1
        
        if len(needToIndex) > 0:
            return -1
        else:
            return chemistry
