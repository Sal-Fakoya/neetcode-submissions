class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)

        # constraint 1: if list is empty
        if length == 0:
            return 0

        # # constraint 2: if list contains one element
        # if length == 1 and nums[length] == val:
        #     return 0
        # elif length == 1 and nums[length] != val:
        #     return 1
        
        # # constraint 3: if list contains all elements == val:
        # if length > 0 and sum(nums) == 0:
        #     return 0
        
        else:
            # skip where an element == val
            non_index = 0
            for index in range(0, length):
                if nums[index] != val:
                    nums[non_index] = nums[index]
                    non_index += 1

            
            print(nums)
            return non_index

