#Problem Link: https://leetcode.com/problems/subarray-product-less-than-k/description/

#Using Sliding Window
#Time Complexity: O(n)

def numSubarrayProductLessThanKII(nums, k):
    if k<=1:
        return 0
    
    n=len(nums)
    
    pd=1
    ans=0
    
    left=0
    right=0
    
    while right<n:
        pd*=nums[right]
        
        while(pd>=k):
            pd/=nums[left]
            left+=1
            
        ans+=right-left+1
        right+=1
    return ans

nums=[int(x) for x in input().split()]
k=int(input())
ans=numSubarrayProductLessThanKII(nums, k)
print(ans)