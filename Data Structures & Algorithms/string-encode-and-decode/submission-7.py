class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = "π"
        encoded = ""
        
        for i, word in enumerate(strs):
            encoded += f"{word}{delimiter}"
        print(encoded)        
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        delimiter = "π"
        split = s.split(delimiter)
        return split[:len(split)-1]
