class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            print(seen)
            if target-nums[i] in seen:
                return [seen[target-nums[i]], i]
            seen[nums[i]] = i
        
        return [0,1]