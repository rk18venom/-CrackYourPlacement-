#Link: https://leetcode.com/problems/count-the-number-of-fair-pairs/description/



#Using Two pointer algorithm

#Solution
def countFairPairs(nums, lower, upper):
    cnt=0
    nums.sort()
    n=len(nums)
    i=0
    j=n-1
    while i!=j:
        s=nums[i]+nums[j]
        if s>upper:
            j-=1
        else:
            cnt+=(j-i)
            i+=1
    cnt1=0
    i=0
    j=n-1
    while i!=j:
        s=nums[i]+nums[j]
        if s<lower:
            cnt1+=(j-i)
            i+=1
        else:
            j-=1
    return cnt-cnt1

#Main
t=int(input())
while t!=0:
    n=int(input())
    nums=list(map(int,input().split()))
    lower=int(input())
    upper=int(input())
    print(countFairPairs(nums,lower,upper))
    t-=1