class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n + 1

        while(right >= left):
            mid = (left + right) // 2
            temp = guess(mid)

            if(temp == -1):
                right = mid - 1
            elif(temp == 1):
                left = mid + 1
            else:
                return mid 