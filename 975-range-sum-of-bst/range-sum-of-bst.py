# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        custom_queue = deque()
        custom_queue.append(root)
        sum_node = 0
        while custom_queue:
            root = custom_queue.popleft()
            if high >= root.val >= low:
                sum_node = sum_node + root.val
            if root.left and root.val > low:
                custom_queue.append(root.left)
            if root.right and root.val < high:
                custom_queue.append(root.right)
        return sum_node 

        

        