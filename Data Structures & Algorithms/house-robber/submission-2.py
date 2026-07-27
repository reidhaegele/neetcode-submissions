class Solution:
    def rob(self, nums: List[int]) -> int:
        
        profits = {}
        def rb(i):
            if i >= len(nums):
                return 0
            if i in profits:
                return profits[i]
            
            profits[i] = max(nums[i] + rb(i+2), rb(i+1))
            return profits[i]
        
        return rb(0)