#Link: https://www.geeksforgeeks.org/problems/implement-atoi/1

#Solution

class Solution:
    def myAtoi(self, s):
        # Code here
        maxi=2**31-1
        mini=(-2)**31
        l=['+','-','1','2','3','4','5','6','7','8','9','0']
        num=0
        sign='+'
        it2=None
        it1=None
        s=s.strip()
        i=0
        for x in s:
            if x in l:
                if x=='-':
                    sign='-'
                    it2=i
                elif x=='+':
                    sign='+'
                else:
                    num=num*10 + int(x)
                    it1=i
            else:
                break
            i+=1
        if num==0:
            s=num
            return s
        else:
            if sign=='-' and it2<it1:
                s= -num
                if s<mini:
                    return mini
                else:
                    return s
            else:
                s=num
                if s>maxi:
                    return maxi
                else:
                    return s
            
                
                
                
                

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")
