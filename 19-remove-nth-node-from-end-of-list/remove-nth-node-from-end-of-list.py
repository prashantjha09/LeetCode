# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast_index = head
        slow_index = head
        counter = 0
        while fast_index.next:
            if counter >= n:
                slow_index = slow_index.next
            fast_index = fast_index.next                
            counter +=1
            
        # Nth node is the head
        if counter + 1 == n:
            return head.next   

        next_index = slow_index.next.next
        slow_index.next = next_index
        return head





        
        


    
        