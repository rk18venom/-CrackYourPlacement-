#Link: https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/description/?envType=daily-question&envId=2024-11-16

#Solution

def resultsArray(nums, k):
    n=len(nums)
    ans=[]
    for i in range(n-k+1):
        x=nums[i]
        cnt=1
        j=i+1
        m=x
        while cnt<k and j<n:
            if x+1==nums[j]:
                m=max(x,m,nums[j])
                x=nums[j]
            else:
                m=-1
                break    
            j+=1
            cnt+=1
        #print(m,i,j)
        ans.append(m)
    return ans  

#Main
t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    k=int(input())
    print(resultsArray(nums,k))  
