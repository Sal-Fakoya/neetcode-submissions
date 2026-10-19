class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length = len(nums)

        # test case: length = 0
        if length == 0:
            return 0
        # constraint: length = 1
        if length == 1:
            return nums[0]

        # constraint: array has all zeros
        if sum(nums) == 0 and max(nums) == 0:
            return 0

        # constaint: array can contain anything
        accumulator = 0
        result = []

        for index in range(0, length-1):
            if nums[index] == 1 and nums[index + 1] == 1 and accumulator==0:
                accumulator = 2
            elif nums[index] == 1 and nums[index + 1] == 1 and accumulator > 0:
                accumulator += 1
            else:
                accumulator = 1
                
            result.append(accumulator)
        return max(result)
            
        
        