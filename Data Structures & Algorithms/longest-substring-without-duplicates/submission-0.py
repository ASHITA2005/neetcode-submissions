class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        n = len(s)
        l = 0
        r = 0
        max_len  = 0
        while l <= r and r < n:
            while r < n and s[r] not in chars:
                chars.add(s[r])
                max_len = max(max_len, r - l + 1)
                r += 1
            chars.remove(s[l])
            l += 1
        return max_len
                
            