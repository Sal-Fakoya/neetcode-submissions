# Definition for singly-linked list.
# class ListNode:i7-1355U7
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
    
        dummy=ListNode()
        tail=dummy

        while left and right:
            if left.val <= right.val:
                tail.next=left
                left=left.next
            else:
                tail.next=right
                right=right.next
            tail=tail.next

        tail.next=left or right

        return dummy.next

