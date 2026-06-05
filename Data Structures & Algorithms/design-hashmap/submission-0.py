class MyHashMap:

    def __init__(self):
        self.map = []

    def put(self, key: int, value: int) -> None:
        temp = [key,value]
        for i in range(len(self.map)):
            if(self.map[i][0] == key):
                self.map[i][1] = value
                return

        self.map.append(temp)
        
    def get(self, key: int) -> int:
        for i in range(len(self.map)):
            if(key == self.map[i][0]):
                return self.map[i][1]
        return -1        

    def remove(self, key: int) -> None:
        for i in range(len(self.map)):
            if(key == self.map[i][0]):
                self.map.pop(i)
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)