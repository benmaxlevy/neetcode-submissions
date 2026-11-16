class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCounts = {}
        tCounts = {}
        for char in s:
            if char not in sCounts:
                sCounts[char] = 1
            else:
                sCounts[char] += 1
        for char in t:
            if char not in tCounts:
                tCounts[char] = 1
            else:
                tCounts[char] += 1
        
        # checking
        sInT = False
        for char in sCounts:
            if char in tCounts and sCounts[char] == tCounts[char]:
                continue
            else:
                return False
        
        sInT = True

        tInS = False
        for char in tCounts:
            if char in sCounts and sCounts[char] == tCounts[char]:
                continue
            else:
                return False
        
        tInS = True

        return sInT and tInS
        