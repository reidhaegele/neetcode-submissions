"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def traverse(curr):

            for child in curr.children:
                traverse(child)
            
            res.append(curr.val)
        
        if not root:
            return []
        traverse(root)
        return res
            