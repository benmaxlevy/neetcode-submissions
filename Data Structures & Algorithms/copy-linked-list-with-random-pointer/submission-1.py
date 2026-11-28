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
            return

        oldToNew = {}

        # first pass: create analogous nodes (no next, random ptrs yet)
        curr = head
        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next
        
        # second pass: now that all nodes are made
        # we can connect them (next, rand) per the mapping
        curr = head
        while curr:
            if curr.next is None:
                oldToNew[curr].next = None
            else:
                oldToNew[curr].next = oldToNew[curr.next]

            if curr.random is None:
                oldToNew[curr].random = None
            else:
                oldToNew[curr].random = oldToNew[curr.random]

            curr = curr.next

        return oldToNew[head]
