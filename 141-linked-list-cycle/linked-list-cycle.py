# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head 
        fast = head
        ''' Run till the fast.next is not null, this validates the case if there is
         no cycle loop will automatically ends andreturn False, else if there is loop 
         then it's definate that the slow will meet fast and then return True '''
        while fast and fast.next:
            slow  = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False    
    

