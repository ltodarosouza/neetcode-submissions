class MinStack:

    def __init__(self):
        self.stack = []
        self.menores = []
    def push(self, val: int) -> None:
        if not self.stack:
            self.menores.append(val)
            self.stack.append(val)
            return
        if val <= self.menores[-1]:
            self.menores.append(val)
        self.stack.append(val)
        return
        

    def pop(self) -> None:
        if self.stack.pop() == self.menores[-1]:
            self.menores.pop()
        return

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.menores[-1]
