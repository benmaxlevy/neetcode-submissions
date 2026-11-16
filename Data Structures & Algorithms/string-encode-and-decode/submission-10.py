class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            prefix = f"#{len(word)}#"
            encoded += f"{prefix}{word}"
        
        return encoded

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        
        decoded = []
        ptr = 0

        while ptr < len(s):
            if s[ptr] == "#":
                end = s.find("#", ptr + 1)
                if end < 0:
                    ptr += 1
                length = int(s[ptr + 1:end])
                decoded.append(s[end+1:end+length+1])

                ptr = end + length + 1
            else:
                ptr += 1
        
        return decoded