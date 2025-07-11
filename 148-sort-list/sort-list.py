# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self,list1,list2):
        l3 = ListNode(0)
        head=l3
        
        while list1 and list2:
            if list1.val<=list2.val:
                l3.next = list1
                list1= list1.next
            else:
                l3.next = list2
                list2 = list2.next
            l3 = l3.next
        l3.next = list1 if list2==None else list2
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