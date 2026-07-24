class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sets = []
        def comb(index: int, sub: list[int], total: int):

            if total == target:
                sets.append(sub.copy())
                return
            if index >= len(nums) or total > target:
                return
            
            sub.append(nums[index])
            comb(index, sub, total + nums[index])
            sub.pop()
            comb(index+1, sub, total)
        
        comb(0, [], 0)
        return sets