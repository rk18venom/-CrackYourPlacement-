#Problem Link: https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def binarySearch(self, s, t):
        n=len(s)
        i=0
        j=n-1
        while i<=j:
            mid=(i+j)//2
            if s[mid]==t:
                return 1
            elif s[mid]<t:
                i=mid+1
            else:
                j=mid-1
        return -1
            

    def nextGreatestLetter(self, s, t):
        m=ord(t)
        p=122
        while m<(p+1):
            curr=chr(m)
            ans=self.binarySearch(s, curr)
            print(ans, curr, t)
            if ans==1 and curr>t:
                return curr
            
            m+=1
        return s[0]
    
s=input()
t=input()
r=Solution()
ans=r.nextGreatestLetter(s, t)
print(ans)