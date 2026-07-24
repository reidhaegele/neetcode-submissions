class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq = set(nums)
        d = {}
        for n in uniq:
            if n+1 in uniq:
                continue
            d[n] = []
            t = n
            while t in uniq:
                d[n].append(t)
                t -= 1
        
        maxi = 0
        for key in d:
            if len(d[key]) >= maxi:
                maxi = len(d[key])
        
        return maxi
        

