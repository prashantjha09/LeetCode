# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        carry = 0
        output_str = []

        while l1 and l2:
            output = carry + l1.val + l2.val

            l1 = l1.next
            l2 = l2.next
            carry = 0

            if output >= 10:
                carry = output // 10
                output = output % 10

            output_str.append(output)

        l = l1 if l1 else l2

        while l:
            output = l.val + carry
            carry = 0

            if output >= 10:
                carry = output // 10
                output = output % 10

            output_str.append(output)
            l = l.next

        if carry:
            output_str.append(carry)

        # Convert the list of digits into a linked list
        dummy = ListNode(0)
        current = dummy

        for digit in output_str:
            current.next = ListNode(digit)
            current = current.next

        return dummy.next
