# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        tail = dummyHead

        curr1 = list1
        curr2 = list2

        while True:
            if curr1 and curr2:
                if curr1.val < curr2.val:
                    new = ListNode(val=curr1.val)
                    tail.next = new
                    tail = new

                    curr1 = curr1.next
                elif curr2.val < curr1.val:
                    new = ListNode(val=curr2.val)
                    tail.next = new
                    tail = new

                    curr2 = curr2.next
                else:                    
                    new2 = ListNode(val=curr2.val)
                    new1 = ListNode(val=curr1.val, next=new2)
                    tail.next = new1
                    tail = new2

                    curr1 = curr1.next
                    curr2 = curr2.next
            elif curr1:
                new = ListNode(val=curr1.val)
                tail.next = new
                tail = new
                curr1 = curr1.next
            elif curr2:
                new = ListNode(val=curr2.val)
                tail.next = new
                tail = new

                curr2 = curr2.next
            else:
                break
        
        return dummyHead.next

    