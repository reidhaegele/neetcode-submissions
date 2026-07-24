class Solution:
    def minWindow(self, s: str, t: str) -> str:
        best = len(s)
        res = ''
        goal = {}
        for c in t:
            goal[c] = goal.get(c, 0) + 1
        freq = {}
        l = 0
        # print(goal)
        for r in range(len(s)):
            # print(f'{s[l:r+1]}')
            
            if s[r] in goal:
                freq[s[r]] = freq.get(s[r], 0) + 1
            # print(freq)
            match = True
            for key in goal:
                if freq.get(key, 0) < goal[key]:
                    match = False
                    break
            if match:
                if r-l+1 <= best:
                    best = r-l+1
                    res = s[l:r+1]
                while True:
                    if s[l] in freq:
                        freq[s[l]] -= 1
                    if s[l] in freq and freq[s[l]] < goal[s[l]]:
                        l += 1
                        break
                    else:
                        l += 1
                        if r-l+1 < best:
                            best = r-l+1
                            res = s[l:r+1]
        
        return res
            
