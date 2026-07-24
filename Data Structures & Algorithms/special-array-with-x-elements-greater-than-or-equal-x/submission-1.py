class Solution:
    def specialArray(self, nums: List[int]) -> int:
        best = -1
        def check(x: int) -> bool:
            above = 0
            for n in nums:
                if n >= x:
                    above += 1
            
            return above == x

        for i in range(len(nums)+1):
            if check(i):
                best = i
        
        return best
            