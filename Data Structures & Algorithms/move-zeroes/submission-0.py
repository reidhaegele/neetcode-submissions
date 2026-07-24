class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = 0
        r = 0

        while l < len(nums)-1:
            if nums[l] != 0:
                l += 1
                continue
            
            r = l+1
            while nums[r] == 0 and r < len(nums)-1:
                r += 1
            if r > len(nums)-1:
                return
            nums[l] = nums[r]
            nums[r] = 0
            l += 1
        
        return
