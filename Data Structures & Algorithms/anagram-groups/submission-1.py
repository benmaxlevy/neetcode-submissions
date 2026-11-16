class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordsByCharCountDicts = {}
        
        for word in strs:
            key = tuple(sorted(word))
            if key not in wordsByCharCountDicts:
                wordsByCharCountDicts[key] = [word]
            else:
                wordsByCharCountDicts[key].append(word)
        
        return list(wordsByCharCountDicts.values())