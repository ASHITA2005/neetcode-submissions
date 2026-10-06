# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root):
            if not root:
                return None

            temp_left = root.left
            temp_right = root.right

            if temp_right:
                root.left = root.right 
            else:
                root.left = None

            if temp_left:
                root.right = temp_left
            else:
                root.right = None

            invert(root.left)
            invert(root.right)

            return root 

        return invert(root)
        
        