from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        window1 = Counter(s1)
        window2 = Counter(s2[:len(s1)])

        if window1 == window2:
            return True

        for j in range(len(s1), len(s2)):
            window2[s2[j]] += 1

            temp = s2[j - len(s1)]
            window2[temp] -= 1

            if window2[temp] == 0:
                del window2[temp]

            if window1 == window2:
                return True

        return False

        
        