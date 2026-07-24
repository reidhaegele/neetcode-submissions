class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        for c in s1:
            freq[c] = freq.get(c, 0) + 1
        
        l = 0
        perm = {}
        for r in range(len(s2)):
            print(f"freq={freq}; perm={perm}")
            if s2[r] not in freq:
                l = r+1
                perm = {}
                continue
            
            perm[s2[r]] = perm.get(s2[r], 0) + 1

            while perm[s2[r]] > freq[s2[r]]:
                perm[s2[l]] -= 1
                l += 1
            
            match = True
            for key in freq:
                if key not in perm or freq[key] != perm[key]:
                    match = False
                    break
            if match:
                return True
        return False


