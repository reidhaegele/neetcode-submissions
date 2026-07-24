class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0
        l = 0
        r = 1
        while r < len(height):
            if height[r] < height[l]:
                r += 1
                continue
            
            trapped += (r-l-1) * min(height[l], height[r])
            l += 1
            while l < r:
                trapped -= height[l]
                l += 1
            r += 1
        
        l = len(height)-1
        r = len(height)-2
        while r > -1:
            if height[r] <= height[l]:
                r -= 1
                continue
            
            trapped += (l-r-1) * min(height[l], height[r])
            l -= 1
            while l > r:
                trapped -= height[l]
                l -= 1
            r -= 1
        
        return trapped