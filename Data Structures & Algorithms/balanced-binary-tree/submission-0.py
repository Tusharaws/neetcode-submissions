# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node: TreeNode):
            if node is None:
                return 0
            
            height_left = check(node.left)
            height_right = check(node.right)
            if height_left == -1 or height_right == -1 or abs(height_left-height_right)>1:
                return -1
            return 1+max(height_left, height_right)
        return check(root)!= -1
            