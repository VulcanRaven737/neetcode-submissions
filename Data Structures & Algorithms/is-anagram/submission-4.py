class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1, s2 = {}, {}

        if len(s) != len(t):
            return False

        for key in range(len(s)):
            s1[s[key]] = 1 + s1.get(s[key], 0)
            s2[t[key]] = 1 + s2.get(t[key], 0)

        return s1 == s2