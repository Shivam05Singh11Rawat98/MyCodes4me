# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or not len(lists):
            return None

        heap=[]
        for i,node in enumerate(lists):
            if node:
                heappush(heap, (node.val,i,node))
        
        t = ListNode()
        head=t
        while heap:
            val,i,node = heappop(heap)
            t.next = ListNode(val)
            t=t.next
            node=node.next
            if node:   
                heappush(heap,(node.val,i,node))
        
        return head.next
