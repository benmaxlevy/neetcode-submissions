# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        currl1 = l1
        currl2 = l2
        carry = 0

        dummy = ListNode()
        curr = dummy

        while currl1 or currl2 or carry:
            val1 = currl1.val if currl1 else 0
            val2 = currl2.val if currl2 else 0
            
            num = val1 + val2 + carry
            currVal = num % 10
            carry = num // 10

            nextNode = ListNode(val=currVal)
            curr.next = nextNode
            curr = nextNode

            if currl1:
                currl1 = currl1.next
            if currl2:
                currl2 = currl2.next

        return dummy.next