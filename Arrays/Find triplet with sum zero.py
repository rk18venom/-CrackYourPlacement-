#GFG POTD: https://practice.geeksforgeeks.org/problems/find-triplets-with-zero-sum/1

def threeSum(nums):
    ans=[]
    nums.sort()
    n=len(nums)
    for i in range(n-1):
        left=i+1
        right=n-1
        while left<right:
            tp=nums[left]+nums[right]+nums[i]
            if tp==0:
                return True
            elif tp<0:
                left+=1
            else:
                right-=1
    return False