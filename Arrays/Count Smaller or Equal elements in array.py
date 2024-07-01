#Problem Link: https://www.naukri.com/code360/problems/count-smaller-or-equal-elements-in-array_1072983?leftPanelTabValue=PROBLEM

from os import *
from sys import *
from collections import *
from math import *

def binary_search(nums,target):

    low=0

    high=len(nums)-1

    while low<=high:

        mid=low+(high-low)//2

        if nums[mid]<=target:

            low=mid+1

        else:

            high=mid-1

    return low

def countSmallerOrEqual(a, b, n, m):
    #  Write your code here
    b.sort()
    res=[]
    for i in range(n):
        x=a[i]
        count=binary_search(b,x)
        res.append(count)
    return res

t=int(input())
while t>0:
    n, m = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    b = list( map(int, input().strip().split()))
    print(countSmallerOrEqual(a, b, n, m))
    t-=1


