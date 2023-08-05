#Problem Link: https://leetcode.com/problems/median-of-two-sorted-arrays/description/

def findMedianSortedArrays(nums1, nums2):
        merged=nums1+nums2
        merged.sort()
        n=len(merged)
        m=n//2
        k=m+1
        if n%2==0:
            return (merged[m-1]+merged[k-1])/2
        else:
            return merged[m]

nums1=[int(x) for x in input().split()]
nums2=[int(x) for x in input().split()]
print("The median is",findMedianSortedArrays(nums1,nums2))
