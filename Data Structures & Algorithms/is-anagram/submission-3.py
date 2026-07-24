class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        f1 = {}
        f2 = {}

        for i in range(len(s)):
            f1[s[i]] = f1.get(s[i], 0) + 1
            f2[t[i]] = f2.get(t[i], 0) + 1
        
        for key in f1:
            if f1.get(key, 'X') != f2.get(key, 'X'):
                return False
        
        return True



        