# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0    
    def averageOfSubtree(self, root: TreeNode) -> int:
        def sum_count(root):
            if root is  None :
                return (0,0)
            left_sum, left_count =  sum_count(root.left) 
            right_sum, right_count  = sum_count(root.right)
            total_sum = left_sum + right_sum + root.val
            total_count = 1 + left_count + right_count
            avg = total_sum // total_count if total_count > 0  else 0

            if avg == root.val:
                self.count += 1   

            return (total_sum, total_count)  

        sum_count(root)
        return self.count        








        