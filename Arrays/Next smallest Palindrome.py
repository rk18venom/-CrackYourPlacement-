#Problem Link: https://practice.geeksforgeeks.org/problems/next-smallest-palindrome4740/1

class Solution:
    def is_palindrome(self, a):
        return a==a[::-1]
    
    def add_1(self, a):
        return str(int(a)+1)
    
    def compare(self, x, y):
        for i , j in zip(x, y):
            if int(i)>int(j):
                return 1
            elif int(i)<int(j):
                return -1
            else:
                continue
        return 0
        
    def handle_odd(self, a):
        n=len(a)
        left=a[:n//2]
        mid=a[n//2]
        right=a[n//2+1:]
        
        if self.compare(left[::-1], right)==1:
            return left + mid + left[::-1]
        else:
            left=left+mid
            left=self.add_1(left)
            return left+left[::-1][1:]
            
    def handle_even(self, a):
        n=len(a)
        left=a[:n//2]
        right=a[n//2:]
        
        if self.compare(left[::-1], right)==1:
            return left + left[::-1]
        else:
            left=self.add_1(left)
            return left+left[::-1]
    
    def solve(self, a):
        if self.is_palindrome(a):
            a=self.add_1(a)
        if len(a) & 1:
            return self.handle_odd(a)
        else:
            return self.handle_even(a)



    def generateNextPalindrome(self,num, n ) :
        # code here
        
        a=""
        for x in num:
            a+=str(x)
        if len(a)==1 and a!='9':
            return self.add_1(a)
        return self.solve(a)
    
n=int(input())
num=[int(x) for x in input().split()]
o=Solution()
print(o.generateNextPalindrome(num, n))