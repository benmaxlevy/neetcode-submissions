# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return

        # reverse, iterate, reverse, return head

        # reverse num. 1
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        reversed_head = prev

        # iterate
        numFromEnd = 1
        curr = prev
        prev = None

        while numFromEnd < n:
            prev = curr
            curr = curr.next
            numFromEnd += 1
        
        if not prev:
            reversed_head = curr.next
        else:
            prev.next = curr.next

        # reverse again
        curr = reversed_head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
