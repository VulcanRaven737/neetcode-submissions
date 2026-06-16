from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        checker = defaultdict(int)

        for k in nums:
            checker[k] += 1

        temp = sorted(checker.items(), key = lambda item:item[1], reverse = True)
        return temp[0][0]
        

        