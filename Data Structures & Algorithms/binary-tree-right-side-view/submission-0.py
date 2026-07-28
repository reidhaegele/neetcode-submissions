# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rights = []

        def traverse(curr, depth):
            if not curr:
                return
            if depth < len(rights):
                rights[depth] = curr.val
            else:
                rights.append(curr.val)
            traverse(curr.left, depth+1)
            traverse(curr.right, depth+1)
        
        traverse(root, 0)
        return rights
        