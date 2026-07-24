class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        #sliding window
        #keep track of freq and current most popular character
        #when r-l+1 - freq[most popular] > k: increment l
        freq = {s[0]: 1}
        best = 1
        popular = s[0]
        l = 0
        for r in range(1, len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            if freq[s[r]] > freq[popular]:
                popular = s[r]
            
            if r-l+1 - freq[popular] > k:
                freq[s[l]] -= 1
                l += 1
            
            best = max(r-l+1, best)
        
        return best