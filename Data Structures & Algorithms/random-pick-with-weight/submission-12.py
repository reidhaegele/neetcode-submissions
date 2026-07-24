import random
class Solution:
    
    def __init__(self, w: List[int]):
        self.l = []
        counter = 0
        for weight in w:
            if weight == 0:
                counter += 1
                continue
            self.l += [counter] * weight
            counter += 1

        

    def pickIndex(self) -> int:
        # print(self.l)
        return self.l[random.randint(0, len(self.l)-1)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()