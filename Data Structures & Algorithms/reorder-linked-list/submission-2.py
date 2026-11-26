# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return

        # first need to find the middle and then reverse it
        
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None

        # reverse right half
        prev = None
        curr = right

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        # prev is head of right half
        # now, time to perform alternating merge

        right = prev
        left = head

        while right:
            temp_left = left.next
            temp_right = right.next

            left.next = right
            right.next = temp_left

            left = temp_left
            right = temp_right
