# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        len_=1
        temp = head
        while temp.next:
            len_+=1
            temp=temp.next
        
        temp.next = head
        k = len_ - k%len_
        while k>0:
            k-=1
            temp=temp.next
        
        head=temp.next
        temp.next=None
        return head