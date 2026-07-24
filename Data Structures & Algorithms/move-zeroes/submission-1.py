class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = 0
        for r in nums:
            if r != 0:
                nums[l] = r
                l += 1
        while l < len(nums):
            nums[l] = 0
            l += 1
        return
