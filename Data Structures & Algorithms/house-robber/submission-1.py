class Solution:
    def rob(self, nums: List[int]) -> int:
        
        profits= {}
        def rb(i):
            if i < 0:
                return 0
            if i in profits:
                return profits[i]
            
            profits[i] = max(rb(i-2) + nums[i], rb(i-1))
            return profits[i]
        
        return rb(len(nums)-1)