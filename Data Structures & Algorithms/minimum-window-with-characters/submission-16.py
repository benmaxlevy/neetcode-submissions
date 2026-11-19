class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        m_left = -1
        m_right = -1

        t_freq = [0] * 100
        missing = len(t)
        
        for char in t:
            t_freq[ord(char) - ord('A')] += 1

        left = 0
        for right in range(len(s)):
            if t_freq[ord(s[right]) - ord('A')] > 0:
                missing -= 1

            t_freq[ord(s[right]) - ord('A')] -= 1

            if missing == 0 and ((m_right == -1 or m_left == -1) or m_right - m_left + 1 > right - left + 1):
                m_left = left
                m_right = right

            while left <= right and missing == 0:
                if (m_right == -1 or m_left == -1) or m_right - m_left + 1 > right - left + 1:
                    m_left = left
                    m_right = right

                t_freq[ord(s[left]) - ord('A')] += 1

                if t_freq[ord(s[left]) - ord('A')] > 0:
                    missing += 1

                left += 1

        return "" if m_left == -1 or m_right == -1 else s[m_left:m_right+1]