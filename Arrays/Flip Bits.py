#Problem Link: https://practice.geeksforgeeks.org/problems/flip-bits0240/1


from sys import maxsize

#Using Kadane's Algorithm

def maxSumSubarray(arr,n):
    maxi=-maxsize
    s=0
    for i in range(n):
        s+=arr[i]
        maxi=max(maxi,s)
        if s<0:
            s=0
    if maxi<0:
        return 0
    return maxi

def flipBits(arr, n): 
    # Write your code here
    arr1=[]
    count=0
    for x in arr:
        if x==1:
            arr1.append(-1)
            count+=1
        else:
            arr1.append(1)
    ans=maxSumSubarray(arr1,n)+count
    return ans

n=int(input())
arr=[int(x) for x in input().split()]
print("Number of ones after fliping the bits {}".format(flipBits(arr,n)))