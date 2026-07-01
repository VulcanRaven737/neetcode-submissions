class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = 0
        left = 0
        window = {}
        maxf = 0

        for right in range(len(s)):
            window[s[right]] = 1 + window.get(s[right], 0)
            maxf = max(maxf, window[s[right]])

            while (right - left + 1) - maxf > k:
                window[s[left]] -= 1
                left += 1
            count = max(count, right - left + 1)

        return count
        