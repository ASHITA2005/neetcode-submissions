class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = collections.defaultdict(int)
        max_freq = 0
        l = 0

        for r in range(len(s)):
            counts[s[r]] += 1
            max_freq = max(max_freq, counts[s[r]])
            
            # Window is invalid, slide the left boundary
            if (r - l + 1) - max_freq > k:
                counts[s[l]] -= 1
                l += 1
                    
        return len(s) - l