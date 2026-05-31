class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalnums=nums1+nums2
        totalnums=sorted(totalnums)
        n=len(totalnums)
        if len(totalnums)%2==0:
            median=(totalnums[n//2]+totalnums[n//2-1])/2
            return median
        else:
            return float(totalnums[n//2])