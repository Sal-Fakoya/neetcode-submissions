
# design linked list class first
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next=next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        # we need both head and tail

        # design head dummy:
        self.left = ListNode()
        self.right = ListNode()

        self.left.next = self.right
        self.right.prev = self.left

        # define a size too:
        self.size=0

    def get(self, index: int) -> int:
        if self.size == 0 or index >= self.size:
            return -1  
        
        curr = self.left
        new_index = index + 1
        for _ in range(new_index):
            curr = curr.next

        return curr.val
        

    def addAtHead(self, val: int) -> None:
        curr = ListNode()
        curr.val = val

        temp = self.left.next
        temp.prev = curr
        curr.next = temp
        self.left.next = curr
        curr.prev = self.left
        self.size += 1
      

    def addAtTail(self, val: int) -> None:
        curr = ListNode()
        curr.val = val
        # create temp node for all items on the left
        temp = self.right.prev
        # point items on left to current
        temp.next = curr
        # point current.prev to items on left
        curr.prev = temp
        # point current.next to the right dummy
        curr.next = self.right
        # point the right.prev to curr
        self.right.prev = curr

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:

        if 0 <= index <= self.size:
            curr = self.left
            prev = ListNode()

            insertion = ListNode()
            insertion.val = val

            # loop to the index
            for _ in range(index+1):
                curr = curr.next
                prev = curr.prev
            
            prev.next = insertion
            insertion.next = curr
            insertion.prev = prev
            curr.prev = insertion
            self.size+=1
            
           

    def deleteAtIndex(self, index: int) -> None:
        if index < self.size and self.size != 0:
            deletion = ListNode()

            # loop to the index
            deletion = self.left
            prev = ListNode()
            rest = ListNode()
            for _ in range(index+1):
                deletion = deletion.next
                prev = deletion.prev
                rest = deletion.next

            prev.next = rest
            rest.prev = prev

            deletion.next = None
            deletion.prev = None
            self.size -= 1
        
                
            
            
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)