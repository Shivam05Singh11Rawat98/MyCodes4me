"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        t1 = head
        list_to_copy = {}
        while t1:
            t2 = Node(t1.val)
            list_to_copy[t1]=t2
            t1 = t1.next
        
        for key,val in list_to_copy.items():
            list_to_copy[key].next = list_to_copy[key.next] if key.next!=None else None
            list_to_copy[key].random = list_to_copy[key.random] if key.random!=None else None
        
        return list_to_copy[head]

        
