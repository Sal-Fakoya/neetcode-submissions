class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans_length = len(nums) * 2
        ans = []

        for index in range(0, ans_length):
            real_iter = index - length
            ans.append(nums[real_iter])

        return ans






        