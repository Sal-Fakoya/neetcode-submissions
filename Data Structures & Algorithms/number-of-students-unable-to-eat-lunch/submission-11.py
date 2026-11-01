# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = None

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # of sandwiches == # of students
        length = len(students)

        # constraint: no elements:
        if length == 0 or len(sandwiches) == 0:
            return None
        elif length == 1 and sandwiches[0] == students[0]:
            return 0
        elif length==1 and sandwiches[0] != students[0]:
            return 1

        # sandwiches are placed in a stack
        # implement sandwiches with list

        # sandwiches[i] is the type of ith sandwich
        # i = 0 means top of the stack
        # top_of_stack = sandwiches[0]

        # studdents are in a queue
        # i.e implement students with linkedlist
        # students[j] is the preference of the jth stdent
        # q = 0 is the front of the queue
        # top_of_queue = ListNode()
        # top_of_queue.next = students

        looper = 0
        acc = 0
        queue_looper=0

        while acc <= (length * 4) and  looper < length:
            top_of_stack = sandwiches[looper]
            top_of_queue = students[queue_looper]

            if top_of_stack == top_of_queue:
                looper += 1
                
            else:
                students.append(top_of_queue)
                acc += 1
            queue_looper += 1
        
        
        return len(sandwiches[looper:])
        

            


                
            



        