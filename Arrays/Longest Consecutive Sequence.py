#Problem Link: https://leetcode.com/problems/longest-consecutive-sequence/
#Problem Link: https://www.naukri.com/code360/problems/longest-consecutive-sequence_759408?leftPanelTabValue=PROBLEM

#Time Complexity: O(n)
#Using Hashing

def longestConsecutiveII(nums):
    dict1={}
    for x in nums:
        if x not in dict1:
            dict1[x]=1
    
    longestStreak=0
    n=len(nums)
    
    for i in range(n):
        curr=nums[i]-1
        if dict1.get(curr,0)==0:
            curr2=nums[i]
            currentStreak=1
            
            while dict1.get(curr2+1,0)==1:
                curr2+=1
                currentStreak+=1
                
            longestStreak=max(currentStreak,longestStreak)
            
    return longestStreak

#Time Complexity: O(nlogn)
#Using Sorted Array

def longestConsecutive(nums):
        s=list(set(nums))
        s.sort()
        n=len(s)
        ans=0
        l=0
        for i in range(0,n):
            if i==0:
                l+=1
            else:
                if s[i]==s[i-1]+1:
                    l+=1
                else:
                    ans=max(l,ans)
                    l=1
        ans=max(ans,l)
        return ans

def lengthOfLongestConsecutiveSequence(arr, n):
    # Write your code here.
    arr.sort()
    dict1={}
    for x in arr:
        dict1[x]=dict1.get(x,0)+1
    
    ans=0
    i=0
    while i<n:
        x=arr[i]
        count=0
        while dict1.get(x,0)!=0:
            count+=1
            x+=1
        ans=max(count,ans)
        i+=count
    return ans
        