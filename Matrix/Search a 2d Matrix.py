#Problem Link: https://leetcode.com/problems/search-a-2d-matrix/submissions/

def bS(arr, x):
        n=len(arr)
        i=0
        j=n-1
        while i<=j:
            mid=(i+j)//2
            if arr[mid]==x:
                return True
            elif arr[mid]<x:
                i=mid+1
            else:
                j=mid-1
        return False

def searchMatrix(matrix, target):
    arr=[]
    n=len(matrix)
    for i in range(n):
        arr+=matrix[i]
    return bS(arr, target)

m=int(input())
n=int(input())
matrix=[[int(x) for x in input().split()] for i in range(m)]
target=int(input())
print(searchMatrix(matrix, target))