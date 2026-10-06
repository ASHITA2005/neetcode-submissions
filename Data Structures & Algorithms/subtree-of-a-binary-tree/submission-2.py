# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSub(r, sr):
            def isIdentical(p, q):
                if not p and not q:
                    return True
                if not p or not q:
                    return False
                return p.val == q.val and isIdentical(p.left, q.left) and isIdentical(p.right, q.right)
            
            if not r:
                return False
            return isIdentical(r, sr) or isSub(r.left, sr) or isSub(r.right, sr) 

        return isSub(root, subRoot)
            
        