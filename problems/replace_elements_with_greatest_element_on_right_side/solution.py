class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_from_right = -1
        for i in range(len(arr) - 1, -1, -1):
            new_max = max(max_from_right, arr[i])
            arr[i] = max_from_right
            max_from_right = new_max
        return arr