#Problem Link: https://leetcode.com/problems/container-with-most-water/description/

def helper(arr, i, j):
    if i>=j:
        return 0
    ans1=-1
    area=abs(i-j)*min(arr[i],arr[j])
    ans=-1
    if arr[i]<=arr[j]:
        ans1=helper(arr, i+1, j)
    else:
        ans1=helper(arr,i,j-1)
    ans=max(ans1,area)
    return ans

def maxArea(height):
    i=0
    j=len(height)-1
    ans=helper(arr, i, j)
    return ans

arr=[int(x) for x in input().split()]
ans=maxArea(arr)
print(ans)