class ListNode:
    def __init__(self, val, nxt, prev):
        self.val = val 
        self.next = nxt
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = ListNode(-1, None, None)
        self.tail = ListNode(-1, self.head, self.head)
        self.head.next, self.head.prev = self.tail, self.tail    
        self.count = k

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            temp = ListNode(value, self.tail, self.tail.prev)
            self.tail.prev.next = temp
            self.tail.prev = temp
            self.count -= 1
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            temp = self.head.next
            self.head.next = temp.next
            temp.next.prev = self.head
            self.count += 1
            return True
        return False  

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.head.next.val   

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.tail.prev.val

    def isEmpty(self) -> bool:
        if self.head.next == self.tail:
            return True
        return False  

    def isFull(self) -> bool:
        if self.count == 0:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()