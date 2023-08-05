#Problem Link: https://leetcode.com/problems/first-missing-positive/description/

#Time Complexity: O(n)

def firstMissingPositive(nums):
    nums.sort()
    dict1={}
    for x in nums:
        if x>=1:
            dict1[x]=dict1.get(x,0)+1
    flag=True
    i=1
    while flag:
        if dict1.get(i,0)==0:
            flag=False
            return i
        i+=1
        
nums=[int(x) for x in input().split()]
print(firstMissingPositive(nums))