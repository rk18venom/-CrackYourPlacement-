#Problem Link: https://www.interviewbit.com/problems/next-similar-number/

#Video Link: https://www.youtube.com/watch?v=LuLCLgMElus

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        l=list(A)
       
        o=[]
        for x in l:
            o.append(x)
        o.sort(reverse=True)
     
        if l==o:
            return -1
        n=len(l)
        k=n-2
        i=n-1
        for k in range(n-2,-1,-1):
            if l[k]<l[k+1]:
                break
        
        if k<0:
            return -1
        else:
            for i in range(n-1,k,-1):
                if l[i]>l[k]:
                    break
            l[k],l[i]=l[i],l[k]
           
            p=l[k+1:]
            l=l[:k+1]+p[::-1]
            num=''
            for j in range(n):
                num+=l[j]
            return num