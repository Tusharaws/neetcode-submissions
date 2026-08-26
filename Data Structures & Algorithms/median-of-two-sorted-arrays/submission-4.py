class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
        m,n  = len(nums1), len(nums2)
        left, right = 0, m
        while left <= right:
            partition1 = (left + right)//2
            partition2 = (m+n+1)//2 - partition1 

            maxLeftA = float('-inf') if partition1==0 else nums1[partition1 - 1] 
            minRightA = float('inf') if partition1==m else nums1[partition1]

            maxLeftB = float('-inf') if partition2==0 else nums2[partition2 - 1] 
            minRightB = float('inf') if partition2==n else nums2[partition2]

            if maxLeftA<=minRightB and maxLeftB<=minRightA:
                if (m+n)%2 != 0:
                    return float(max(maxLeftA, maxLeftB))
                else:
                    return (max(maxLeftA, maxLeftB)+ min(minRightA, minRightB)) / 2.0
            elif maxLeftA>minRightB:
                right = partition1 - 1
            else:
                left = partition1 + 1 