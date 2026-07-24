from heapq import heappush,heappop
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        h = []
        res = []

        for i in range(k-1):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
            heappush(h, -nums[i])
        
        for r in range(k-1, len(nums)):
            
            freq[nums[r]] = freq.get(nums[r], 0) + 1
            heappush(h, -nums[r])
            
            ans = -heappop(h)
            while freq[ans] <= 0:
                ans = -heappop(h)
            
            res.append(ans)
            freq[nums[r-k+1]] -= 1
            if freq[ans] > 0: 
                heappush(h, -ans)
        
        return res
            

