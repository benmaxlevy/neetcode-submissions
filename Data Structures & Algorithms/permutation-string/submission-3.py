class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_freq = defaultdict(int)
        s2_freq = defaultdict(int)
        for char in s1:
            s1_freq[char] += 1
        
        print(s1_freq)

        left = 0
        for right in range(len(s2)):
            s2_freq[s2[right]] += 1
            print(left, right, s2_freq)
            if s2_freq == s1_freq:
                return True
            while left < right and (right - left + 1 >= len(s1) or s2[left] not in s1):
                s2_freq[s2[left]] -= 1
                if s2_freq[s2[left]] == 0:
                    del s2_freq[s2[left]]
                left += 1

            
           
        return False