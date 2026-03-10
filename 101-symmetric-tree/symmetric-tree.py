# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        pairs = [(root.left,root.right)]
        i = 0

        while i < len(pairs):
            a,b = pairs[i]
            i += 1
            if not a and not b:
                continue
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            
            pairs.append((a.left,b.right))
            pairs.append((a.right,b.left))
            
        return True