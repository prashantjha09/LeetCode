# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        node_dic = {}
        pointer = head
        while pointer:
            node_dic[pointer] = pointer.val
            pointer = pointer.next
        node_dic = dict(sorted(node_dic.items(), key = lambda node_dic_items : node_dic_items[1]))
        node_list = list(node_dic.keys())
        for index in range(len(node_list)):
            if index == len(node_list)-1:
                node_list[index].next = None  
            else:              
                node_list[index].next = node_list[index+1]
            index=index+1   
        return node_list[0]