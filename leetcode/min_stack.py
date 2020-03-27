from math import inf


class MinStack:
    """The time complexity of all operations is O(1)."""

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = inf

    def push(self, x: int) -> None:
        # Store the value along with the previous min value
        self.stack.append((x, self.min))
        if x < self.min:
            self.min = x

    def pop(self) -> None:
        value, self.min = self.stack.pop()
        return value

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min