class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.prefix_min or val < self.prefix_min[-1]:
            self.prefix_min.append(val)
        else:
            self.prefix_min.append(self.prefix_min[-1])
    def pop(self) -> None:
        self.stack.pop()
        self.prefix_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix_min[-1]
        
