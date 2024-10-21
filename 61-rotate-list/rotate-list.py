# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if k == 0:
        #     return head
        link_list_length = 0
        pointer = head
        while pointer:
            pointer = pointer.next
            link_list_length +=1  
    
        if link_list_length <= 1:
            return head

        effective_k = k if k <= link_list_length else k % link_list_length            
        if effective_k == link_list_length or effective_k == 0:
            return head

        counter = 0
        pointer1 = head 
        pointer2 = head
        while pointer1.next:
            pointer1 = pointer1.next
            counter +=1
            if counter >= effective_k+1:
                pointer2 = pointer2.next    

        tmp_head = pointer2.next
        pointer2.next = None
        pointer1.next = head
        return tmp_head
                  




