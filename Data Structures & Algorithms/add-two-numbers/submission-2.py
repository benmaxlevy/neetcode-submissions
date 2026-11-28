# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        place = 1
        curr = l1

        while curr:
            num1 += place * curr.val
            curr = curr.next
            place *= 10

        num2 = 0
        place = 1
        curr = l2

        while curr:
            num2 += place * curr.val
            curr = curr.next
            place *= 10

        result = num1 + num2

        if result == 0:
            return ListNode(val=0)

        # start with dummy node - will return dummy.next (head)
        dummy = ListNode()
        curr = dummy

        while result > 0:
            val = result % 10
            result //= 10
            
            nextNode = ListNode(val=val)
            curr.next = nextNode
            curr = nextNode
        
        return dummy.next
