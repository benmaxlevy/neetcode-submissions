class MinStack:

    def __init__(self):
        self.data = []
        self.mins = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if len(self.mins) == 0 or self.mins[-1] > val:
            self.mins.append(val)
        else:
            self.mins.append(self.mins[-1])

    def pop(self) -> None:
        self.mins.pop()
        return self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.mins[-1]
