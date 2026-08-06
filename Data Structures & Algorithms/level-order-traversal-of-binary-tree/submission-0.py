# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def traverse(curr, d):
            if not curr:
                return
            if len(res)-1 < d:
                res.append([])
            res[d].append(curr.val)
            traverse(curr.left, d+1)
            traverse(curr.right, d+1)
        
        traverse(root, 0)
        return res

