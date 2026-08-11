class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp = "".join(sorted(s))
        temp2 = "".join(sorted(t))

        return temp == temp2