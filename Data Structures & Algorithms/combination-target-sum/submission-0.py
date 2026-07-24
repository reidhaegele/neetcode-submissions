class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sets = []
        def comb(index: int, sub: list[int], total: int):

            if total == target:
                if sub in sets:
                    return
                sets.append(sub.copy())
            if total > target:
                return

            if index >= len(nums):
                return
            
            comb(index+1, sub, total)
            total += nums[index]
            sub.append(nums[index])
            comb(index, sub, total)
            comb(index+1, sub, total)
            sub.pop()
        
        comb(0, [], 0)
        return sets