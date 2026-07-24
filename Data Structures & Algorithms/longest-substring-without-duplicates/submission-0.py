class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        l = 0
        freq = {}
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            while freq[s[r]] > 1:
                freq[s[l]] -= 1
                l += 1
            best = max(r-l+1, best)
     
        return best