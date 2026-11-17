class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        max_length = 0
        seen = set()
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

            if len(s) == max_length:
                return max_length
            
        return max_length