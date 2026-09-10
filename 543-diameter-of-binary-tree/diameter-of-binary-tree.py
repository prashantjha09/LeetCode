# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dp = {}
        self.diameter = {}
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def subtree_max(root):
            if root is None:
                return 0
            if root in self.dp:
                return self.dp[root]
            left_count  =  subtree_max(root.left)  
            right_count =  subtree_max(root.right)   
            max_count  =  max(left_count, right_count) + 1
            self.diameter[root] = left_count + right_count
            self.dp[root] = max_count
            return max_count

        subtree_max(root)
        return max(self.diameter.values()) 





        