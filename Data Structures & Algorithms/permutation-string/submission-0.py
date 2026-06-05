from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check = defaultdict(int)
        check2 = set(s1)

        for i in range(len(s1)):
            check[s1[i]] += 1

        left = 0
        right = 0
        count = []
        count.append(0)

        while(right < len(s2) and max(count) <= len(s1)):
            if(s2[left] not in check2 and s2[right] not in check2):
                left += 1
                right += 1
                continue

            elif(s2[right] in check and check[s2[right]] > 0):
                count[-1] += 1
                check[s2[right]] -= 1
                right += 1                
            else:
                check[s2[left]] += 1
                left += 1
                count.append(right - left)

        if(max(count) >= len(s1)):
            return True
        return False
            


