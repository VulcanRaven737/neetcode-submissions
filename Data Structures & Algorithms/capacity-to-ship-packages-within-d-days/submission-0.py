class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        res = right

        while left <= right:
            mid = (left + right) // 2
            temp = self.howmanydays(weights, mid)


            if temp > days:
                left = mid + 1
            else:
                res = min(res, mid)
                right = mid - 1

        return res

    
    def howmanydays(self, weights, capacity):
        days = 1
        curr = 0
    
        for w in weights:
            if curr + w > capacity:
                days += 1
                curr = 0
            curr += w
    
        return days
        