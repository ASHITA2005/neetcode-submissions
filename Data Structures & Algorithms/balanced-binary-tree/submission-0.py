# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isBal(root):
            def getHeight(r):
                if not r:
                    return 0
                return 1 + max(getHeight(r.right), getHeight(r.left))

            if not root:
                return True

            left = getHeight(root.left)
            right = getHeight(root.right)

            return abs(left-right) <= 1 and isBal(root.left) and isBal(root.right)
        return isBal(root)
        