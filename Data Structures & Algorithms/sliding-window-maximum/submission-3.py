from heapq import heappush,heappop
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        res = []
        
        for r in range(len(nums)):
            heappush(h, (-nums[r], r))
            
            if r >= k-1:
                while h[0][1] <= r-k:
                    heappop(h)

                res.append(-h[0][0])
        
        return res