class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        for index in range(0, length - 1):
            arr[index] = max(arr[index + 1:])

        arr[length - 1] = -1
        return arr
        