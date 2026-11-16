class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordsByCharCount = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            wordsByCharCount[tuple(freq)].append(word)

        return list(wordsByCharCount.values())