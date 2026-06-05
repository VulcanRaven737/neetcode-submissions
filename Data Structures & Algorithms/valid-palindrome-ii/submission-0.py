class Solution:
    def validPalindrome(self, s: str) -> bool:
        head = 0
        tail = len(s) - 1

        while(tail > head):
            if(s[head] == s[tail]):
                head += 1
                tail -= 1
                continue
            else:
                skip_head = s[head+1 : tail+1] == s[head+1 : tail+1][::-1]
                skip_tail = s[head : tail] == s[head : tail][::-1]
                return skip_head or skip_tail

        return True
        
