# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sum_list = []
        def get_sum_of_levels(input_queue):
            tmp_queue = deque()
            level_sum = 0
            while input_queue:
                node = input_queue.popleft()
                level_sum += node.val
                if node.left :
                    tmp_queue.append(node.left)
                if node.right:
                    tmp_queue.append(node.right)      
            sum_list.append(level_sum)
            if tmp_queue:
                get_sum_of_levels(tmp_queue)
    
        bfs_queue = deque([root])
        listval = get_sum_of_levels(bfs_queue)
        sorted_list = list(sorted(sum_list))
        if len(sorted_list)<k:
            return -1
        return sorted_list[-k]











        