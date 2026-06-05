class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        head = 0
        tail = -1

        for i in range(len(s)//2):
            temp_val = s[head]
            s[head] = s[tail]
            s[tail] = temp_val
            head += 1
            tail -= 1