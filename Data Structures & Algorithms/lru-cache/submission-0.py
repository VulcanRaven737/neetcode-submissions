class Node:
    def __init__(self, key, value, nxt, prev):
        self.key = key
        self.val = value
        self.next = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, -1, None, None)
        self.tail = Node(-1, -1, self.head, self.head)
        self.head.next, self.head.prev = self.tail, self.tail
        self.map = {}
        self.cap = capacity

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def insert(self, node):
        prev = self.tail.prev

        prev.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.map:
            temp = self.map[key]
            self.remove(temp)
            self.insert(temp)
            return temp.val
        else:
            return -1                

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            temp = self.map[key] 
            temp.val = value
            self.remove(temp)
            self.insert(temp)
            return

        if len(self.map) == self.cap:
            temp = self.head.next
            self.remove(temp)
            del self.map[temp.key]

        node = Node(key, value, None, None)
        self.insert(node)
        self.map[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)