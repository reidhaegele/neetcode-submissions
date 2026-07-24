class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + '#' + s)
        return "".join(res)
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            h = s.find('#', i)
            l = int(s[i:h])
            res.append(s[h+1:h+l+1])
            i = h+l + 1
        return res