class FreqStack:

    def __init__(self):
        self.max_count = 0
        self.stacks = {}
        self.count = {}

    def push(self, val: int) -> None:
        total = 1 + self.count.get(val, 0)
        self.count[val] = total
        if total > self.max_count:
            self.max_count = total
            self.stacks[total] = []

        self.stacks[total].append(val)         

    def pop(self) -> int:
        ret = self.stacks[self.max_count].pop()
        self.count[ret] -= 1

        if not self.stacks[self.max_count]:
            self.stacks.pop(self.max_count)
            self.max_count -= 1

        return ret


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()