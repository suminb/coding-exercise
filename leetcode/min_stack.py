from math import inf


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = inf

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x < self.min:
            self.min = x

    def pop(self) -> None:
        value = self.stack.pop()
        if value == self.min:
            # TODO: Can we do this faster than O(n)?
            if self.stack:
                self.min = min(self.stack)
            else:
                self.min = inf
        return value

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min