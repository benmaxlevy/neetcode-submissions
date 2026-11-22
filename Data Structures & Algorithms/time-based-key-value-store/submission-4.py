class TimeMap:
    # map keys to list (of (value, timestamp) pairs)
    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((value, timestamp))
        else:
            self.time_map[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""

        pairs = self.time_map[key]
        left = 0
        right = len(pairs) - 1

        curr = None

        while left <= right:
            mid = (left + right) // 2
            
            if pairs[mid][1] == timestamp:
                return pairs[mid][0]
            elif pairs[mid][1] < timestamp:
                curr = pairs[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return curr if curr is not None else ""