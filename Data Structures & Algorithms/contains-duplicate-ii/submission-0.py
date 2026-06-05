from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        slow = 0
        fast = 1
        check = defaultdict(int)

        if(k == 0):
            return False

        check[nums[0]] += 1

        while(fast < len(nums)):
            val = check[nums[fast]]
            if(fast - slow <= k and val > 0):
                return True
            elif(fast - slow <= k and val < 1):
                check[nums[fast]] += 1
                fast += 1
            else:
                check[nums[slow]] -= 1
                slow += 1   

        return False
        