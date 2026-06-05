class Solution:
    def isPalindrome(self, s: str) -> bool:
        proc_str = ""
        low = "abcdefghijklmnopqrstuvwxyz0123456789"
        for i in range(len(s)):
            if(s[i].lower() in low):
                proc_str += s[i].lower()
        if(proc_str[::-1] == proc_str):
            return True
        return False