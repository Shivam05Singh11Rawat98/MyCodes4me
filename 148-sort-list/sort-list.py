# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self,list1,list2):
        l3 = ListNode(0)
        head=l3
        l1=list1
        l2=list2
        while l1!=None or l2!=None:
            if l1==None:
                while l2!=None:
                    l3.next = ListNode(l2.val)
                    l2 = l2.next
                    l3 = l3.next
            elif l2==None:
                while l1!=None:
                    l3.next = ListNode(l1.val)
                    l1 = l1.next
                    l3 = l3.next
            else:
                if l1.val>l2.val:
                    l3.next = ListNode(l2.val)
                    l2 = l2.next
                    l3 = l3.next
                else:
                    l3.next = ListNode(l1.val)
                    l1 = l1.next
                    l3 = l3.next

        return head.next
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = ListNode(0)
        prev.next = head

        here = head

        while here and here.next:
            here = here.next.next
            prev = prev.next
        
        head2 = prev.next
        prev.next=None
        leftSide = self.sortList(head)
        rightSide = self.sortList(head2)

        return self.merge(leftSide,rightSide)