#Problem Link: https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string-1587115620/1

from itertools import permutations

def permutation(s):
    p=permutations(s)
    d=[]
    for l in p:
        d.append("".join(l))
    d.sort()
    return d
    
s=input()
print(*permutation(s),sep="\n")