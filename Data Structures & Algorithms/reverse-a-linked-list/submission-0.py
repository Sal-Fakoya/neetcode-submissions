# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        future = None

        while current:
            future = current.next # saves the rest of the list
            current.next = prev # flips the pointer
            prev = current # moves prev forward
            current = future # moves current forward
         
        head = prev
        return prev

        