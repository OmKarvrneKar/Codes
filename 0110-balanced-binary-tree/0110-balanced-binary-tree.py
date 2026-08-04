# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(node):
            if not node:
                return 0
            
            # 1. Check left subtree balance and height
            left_height = dfs(node.left)
            if left_height == -1:
                return -1
                
            
            right_height = dfs(node.right)
            if right_height == -1:
                return -1
            
            # 3. Check current node balance
            if abs(left_height - right_height) > 1:
                return -1
                
            # 4. Return actual height to parent node
            return 1 + max(left_height, right_height)
            
        return dfs(root) != -1
        