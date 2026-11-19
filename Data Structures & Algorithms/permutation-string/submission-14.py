class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq = [0] * 26
        s2_freq = [0] * 26
        
        for char in s1:
            s1_freq[ord(char) - ord('a')] += 1

        left = 0

        for right in range(len(s2)):
            s2_freq[ord(s2[right]) - ord('a')] += 1
            while left < right and (right - left + 1 > len(s2) or s2_freq[ord(s2[left]) - ord('a')] > s1_freq[ord(s2[left]) - ord('a')]):
                s2_freq[ord(s2[left]) - ord('a')] -= 1
                left += 1

            if s2_freq == s1_freq:
                return True

        return False