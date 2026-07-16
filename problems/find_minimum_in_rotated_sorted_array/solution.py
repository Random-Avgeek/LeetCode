class Solution:
    def findMin(self, arr: List[int]) -> int:
        if len(arr)==1:
            return arr[0]
        if arr[0]<arr[-1]:
            return arr[0] #edge case for sorted array
        low=0
        high=len(arr)-1
        while low <= high:
            mid = (low + high)//2

            if mid < len(arr)-1 and arr[mid]>arr[mid+1]:
                return arr[mid+1]
            if mid > 0 and arr[mid-1]>arr[mid]:
                return arr[mid]

            if arr[mid] < arr [high]:
                high = mid -1
            else:
                low=mid+1
        return arr[low]