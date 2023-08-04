#Problem Link: https

def productExceptSelf(nums):
    zero=0
    n=len(nums)
    for i in range(n):
        if nums[i]==0:
            zero+=1
    if zero==0:
        pd1=1
        for i in range(n):
            pd1*=nums[i]
        ans=[]
        for i in range(n):
            ans.append(pd1//nums[i])
        return ans
    elif zero==1:
        pd1=0
        pd2=1
        for i in range(n):
            if nums[i]!=0:
                pd2*=nums[i]
        ans=[]
        for i in range(n):
            if nums[i]==0:
                ans.append(pd2)
            else:
                ans.append(pd1)
        return ans
    else:
        ans=[0]*n
        return ans

arr=[int(x) for x in input().split()]
ans=productExceptSelf(arr)
print(ans)

