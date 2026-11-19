class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        m_left = -1
        m_right = -1

        s_freq = [0] * 100
        t_freq = [0] * 100
        t_freq_indexes = set()
        
        for char in t:
            t_freq[ord(char) - ord('A')] += 1
            t_freq_indexes.add(ord(char) - ord('A'))
        
        left = 0
        for right in range(len(s)):
            if t_freq[ord(s[right]) - ord('A')] > 0:
                s_freq[ord(s[right]) - ord('A')] += 1

            if s_freq == t_freq and ((m_right == -1 or m_left == -1) or m_right - m_left + 1 > right - left + 1):
                m_left = left
                m_right = right

            enough = True
            for index in t_freq_indexes:
                if s_freq[index] < t_freq[index]:
                    enough = False
                    break

            while left <= right and enough:
                if (m_right == -1 or m_left == -1) or m_right - m_left + 1 > right - left + 1:
                    m_left = left
                    m_right = right

                if t_freq[ord(s[left]) - ord('A')] > 0 and s_freq[ord(s[left]) - ord('A')] > 0:
                    s_freq[ord(s[left]) - ord('A')] -= 1

                left += 1

                enough = True
                for index in t_freq_indexes:
                    if s_freq[index] < t_freq[index]:
                        enough = False
                        break

        return "" if m_left == -1 or m_right == -1 else s[m_left:m_right+1]