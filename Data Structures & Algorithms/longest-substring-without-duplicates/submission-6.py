class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        max_length = 0
        freq = defaultdict(int)
        left = 0

        for right in range(len(s)):
            freq[s[right]] += 1
            while freq[s[right]] > 1:
                left += 1
                freq[s[left-1]] -= 1
            max_length = max(max_length, right - left + 1)
            
        return max_length