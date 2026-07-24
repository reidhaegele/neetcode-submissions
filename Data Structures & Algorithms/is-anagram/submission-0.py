class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sf = {}
        tf = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            sf[s[i]] = sf.get(s[i], 0) + 1
            tf[t[i]] = tf.get(t[i], 0) + 1
        
        for k in sf:
            if sf.get(k, 0) != tf.get(k, -1):
                return False
        
        return True