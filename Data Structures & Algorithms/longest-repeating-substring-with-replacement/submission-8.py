class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        
        freq = defaultdict(int)

        max_len = 0

        left = 0

        for right in range(len(s)):
            freq[s[right]] += 1
            replacements = right - left + 1 - max(freq.values())

            while left < right and replacements > k:
                freq[s[left]] -= 1
                left += 1
                replacements = right - left + 1 - max(freq.values())
                
            max_len = max(max_len, right - left + 1)

        return max_len