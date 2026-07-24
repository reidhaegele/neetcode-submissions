class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            k = "".join(sorted(word))
            if k in anagrams:
                anagrams[k].append(word)
            else:
                anagrams[k] = [word]
        
        return list(anagrams.values())