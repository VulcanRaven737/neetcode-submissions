class StockSpanner:

    def __init__(self):
        self.stack = []
        
    def next(self, price: int) -> int:
        temp_span = 1
        while self.stack and self.stack[-1][0] <= price:
            val_list = self.stack.pop()
            temp_span += val_list[1]

        self.stack.append([price, temp_span])
        return temp_span       


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)