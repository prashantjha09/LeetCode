# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
custom_queue = deque()
from collections import deque
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        custom_queue.append(root)
        sum_node = []
        while custom_queue:
            root = custom_queue.pop()
            if high >= root.val >= low:
                sum_node.append(root.val)
            if root.left:
                custom_queue.append(root.left)
            if root.right:
                custom_queue.append(root.right)
        return sum(sum_node)        

        

        