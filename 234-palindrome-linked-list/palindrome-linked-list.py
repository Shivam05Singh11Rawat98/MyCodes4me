# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
prev=None
1->None
1->2
tor->2
hare->
"""
class Solution:
    def reverse_(self,head):
        #2
        prev = None
        while head:
            next_node = head.next
            head.next=prev
            prev=head
            head=next_node
        
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        tor,hare = head,head
        # 1->2->2->1
        while hare and hare.next:
            hare=hare.next.next
            tor=tor.next
        
        hare=head
        tor = self.reverse_(tor)

        while hare and tor:
            if hare.val!=tor.val:
                return False
            hare=hare.next
            tor=tor.next
        
        return True
