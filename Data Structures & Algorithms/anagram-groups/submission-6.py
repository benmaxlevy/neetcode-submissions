class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        sortedStrs = []

        for i in range(len(strs)):
            sortedStrs.append(''.join(sorted(strs[i].lower())))

        for i in range(len(sortedStrs)):
            if sortedStrs[i] not in groups:
                groups[sortedStrs[i]] = []
            groups[sortedStrs[i]].append(strs[i])

        result = []

        for word in groups:
            result.append(groups[word])
        
        return result