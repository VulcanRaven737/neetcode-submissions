import math
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_stack.append(math.inf)

    def push(self, val: int) -> None:
        self.stack.insert(0, val)
        minimum = min(self.min_stack[0], val)
        if(minimum == val):
            self.min_stack.insert(0, minimum)

    def pop(self) -> None:
        if(self.stack[0] == self.min_stack[0]):
            self.min_stack.pop(0)
        self.stack.pop(0)                

    def top(self) -> int:
        return self.stack[0]        

    def getMin(self) -> int:
        return self.min_stack[0]         
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
