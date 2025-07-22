# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
l1 -> 9->None
l2 -> 1->None
output-> 0
carry = 1
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        output = ListNode(0)
        temp = output
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            sum_val = a + b + carry
            carry = sum_val//10
            temp.next = ListNode(sum_val%10)
            temp=temp.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        
        if carry==1:
            temp.next = ListNode(1)
        
        return output.next