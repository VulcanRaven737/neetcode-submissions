class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = 0
        fast = 0
        seen = set()
        count = 0

        while (fast < len(s)):
            while(s[fast] in seen):
                seen.remove(s[slow])
                slow += 1
            seen.add(s[fast])
            count = max(count, fast - slow + 1)
            fast += 1

        return count

        