import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []

        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for key in freq:
            heapq.heappush(h, (-freq[key], key))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(h)[1])
        
        return res
        
        