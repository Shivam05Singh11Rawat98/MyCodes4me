# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        merged_list = ListNode(-1)
        temp = merged_list
        for i,node in enumerate(lists):
            if node:
                heappush(min_heap,(node.val,i,node))
        
        while min_heap:
            val,i,node = heappop(min_heap)
            temp.next = ListNode(val)
            temp = temp.next
            if node.next:
                heappush(min_heap,(node.next.val,i,node.next))

        return merged_list.next


"""
l1->1->2->3
l2->4->5->6
l3->7->8->9
[(2,0),(4,1),(7,8)]
lk -> 1->2
"""