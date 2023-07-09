#Problem Link: https://practice.geeksforgeeks.org/problems/smallest-positive-missing-number-1587115621/1

def missingNumber(arr):
        #Your code here
        m=1
        l=set(arr)
        l=list(l)
        l.sort()
        
        for x in l:
            if x>0:
                if x==m:
                    m+=1
                else:
                    return m
        return m

n=int(input())
arr=[int(x) for x in input().split()]
print("Smallest positive number that is not present:",missingNumber(arr))