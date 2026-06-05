class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checker1 = {}
        checker2 = {}
        for i in s:
            if i not in checker1:
                checker1[i] = 1
            else: 
                checker1[i] += 1
        for j in t:
            if j not in checker2:
                checker2[j] = 1
            else:
                checker2[j] += 1
                
        return checker1 == checker2
        