# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head:
            return head
        
        cnt = 0
        temp = head

        while temp:
            temp = temp.next
            cnt+=1

        dummy = ListNode(-1)
        dummy.next = head
        prev=dummy
        while cnt>=k:
            curr = prev.next
            nxt = curr.next
            for _ in range(1,k):
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = curr.next
            prev=curr
            cnt-=k
        
        return dummy.next

