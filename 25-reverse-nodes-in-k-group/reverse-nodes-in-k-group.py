# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #len of list
        n=0
        curr = head
        while curr:
            n+=1
            curr=curr.next
        n = n//k

        dummy = ListNode(-1)
        prev = dummy
        dummy.next = head

        while n!=0:
            curr = prev.next
            next = curr.next
            temp_k = k-1
            while temp_k!=0:
                curr.next = next.next
                next.next = prev.next
                prev.next = next
                next = curr.next
                temp_k-=1
            prev = curr
            n-=1
        
        return dummy.next
            

"""
k=3
t_k = 0
-1->3->2->1->6->5->4->None
prev = 1->
curr = 
next = None
n = 1
"""