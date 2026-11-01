class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)

        list_nums = [(index, value) for index, value in enumerate(nums)]

        nums = sorted(nums)
        acc = 0
        starter = 0
        ender = length - 1


        while starter < ender:
            acc = nums[starter] + nums[ender]

            if acc < target:
                starter += 1
            elif acc > target:
                ender -= 1
            else:
                break
        
        starter = nums[starter]
        ender = nums[ender]

        left = None
        right = None
        for i in range(length):
            key, val = list_nums[i]

            if val == starter and left is None:
                left = key
            elif val == ender and right is None:
                right = key
        
        # print(left, right)
        
        
        return sorted([left, right])

            




        