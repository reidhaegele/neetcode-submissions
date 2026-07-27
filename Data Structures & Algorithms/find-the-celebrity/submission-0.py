# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        l = 0
        r = 1
        while r < n:
            if l == r:
                r += 1
                continue
            if knows(l, r):
                l += 1
            else:
                r += 1

        for i in range(n):
            if i == l:
                continue
            if not knows(i, l) or knows(l, i):
                return -1
        
        return l