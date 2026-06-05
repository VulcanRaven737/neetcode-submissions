from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        slow = 0
        counts = defaultdict(int)
        
        max_freq = 0
        max_len = 0

        for fast in range(len(s)):
            counts[s[fast]] += 1
            max_freq = max(max_freq, counts[s[fast]])

            while (fast - slow + 1) - max_freq > k:
                counts[s[slow]] -= 1
                slow += 1

            max_len = max(max_len, fast - slow + 1)

        return max_len

        