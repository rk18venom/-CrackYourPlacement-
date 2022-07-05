#Problem Link: https://leetcode.com/problems/merge-sorted-array/

def merge(nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr=nums1[:m]+nums2
        arr.sort()
        for i in range(n+m):
            nums1[i]=arr[i]