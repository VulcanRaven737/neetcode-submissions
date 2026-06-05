class MyHashSet:

    def __init__(self):
        self.max = 10000
        self.buckets = [[] for i in range(self.max)]

    def add(self, key: int) -> None:
        index = key % self.max
        bucket = self.buckets[index]

        if(key not in bucket):
            bucket.append(key)

    def remove(self, key: int) -> None:
        index = key % self.max
        bucket = self.buckets[index]

        if(key in bucket):
            bucket.remove(key)
            return
        
    def contains(self, key: int) -> bool:
        index = key % self.max
        bucket = self.buckets[index]

        if (key in bucket):
            return True
        return False 
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)