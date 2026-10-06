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
            
            if isIdentical(r, sr):
                return True
            if r.left and isSub(r.left, sr):
                return True
            if r.right and isSub(r.right, sr):
                return True
            return False

        return isSub(root, subRoot)
            
        